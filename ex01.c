int calcula_total_leds(int altura,int largura)
{
  int resultado = 0;
  
  if (altura <= 0 || largura <= 0)
    return (0);
  resultado = (largura + 1) * (altura  + 1);
  return (resultado);
}