const express = require("express");

const createServer = (pool, port = 3000) => {
  const app = express();
 
const buildCommentsTree = (comments) => {
    const commentMap = new Map();
    comments.forEach((comment) => {
        comment.children = [];
        commentMap.set(comment.id, comment);
    });

    const rootComments = [];
    comments.forEach((comment) => {
        if (comment.parent_id === null) {
            const { parent_id, ...rootComment } = comment;
            rootComments.push(rootComment);
        } else {
            const parent = commentMap.get(comment.parent_id);
            if (parent) {
                parent.children.push(comment);
            }
        }
    });

    rootComments.forEach(comment => {
        if (comment.children && comment.children.length === 0) {
            delete comment.children
        }
    });

    return rootComments;
};
  
  app.get("/posts/:id/comments", async (req, res) => {
    const postId = parseInt(req.params.id, 10);

    try {
      const result = await pool.query(
        "SELECT id, text, parent_id FROM comments WHERE post_id = $1 ORDER BY id",
        [postId]
      );
      const comments = result.rows;

      if (comments.length === 0) {
        return res.status(404).send("Post not found");
      }
      const commentsTree = buildCommentsTree(comments);
      res.json({ data: commentsTree });
    } catch (err) {
      console.error("Error querying the database", err);
      res.status(500).send("Internal Server Error");
    }
  });

  const server = app.listen(port, () =>
    console.log(`[server] listening on port ${port}`)
  );
  return {
    app,
    close: () =>
      new Promise((resolve) => {
        server.close(() => {
          resolve();
          console.log("[server] closed");
        });
      }),
  };
};

module.exports = { createServer };
