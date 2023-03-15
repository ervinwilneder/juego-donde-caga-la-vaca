prompt for chatGPT4:

> Escribe un juego en python dadas las siguientes instrucciones:
>
> El juego se llama "Donde caga la vaca"
> 
> El juego se compone de una grilla de 10x10 (cada celda se denomina parcela, con lo cual la grilla tiene 100 parcelas) en donde una "vaca" es liberada en alguna de las 
> parcelas externas.
>
> La vaca puede moverse, descansar, comer o hacer popó.
>
> La probabilidades iniciales en la primer parcela son:
> mover: 0.8
> descansar: 0.05
> comer: 0.1
> popó: 0.05
> 
> Luego, el comportamiento de la vaca se modela como una cadena de markov definida a través de la siguiente matriz:
> |        | mover | descansar | comer | popó |
> |--------|-------|-----------|-------|------|
> | mover  | 0.5   | 0.2       | 0.2   | 0.1  |
> | descansar | 0.6   | 0.2       | 0.1   | 0.1  |
> | comer  | 0.1   | 0.6       | 0.2   | 0.1  |
> | popó   | 0.8   | 0.1       | 0.05  | 0.05 |
> 
> En cada instante de tiempo:
>
> cuando la vaca se mueve lo hace a cualquiera de las parcelas adyacentes
>
> cuando la vaca descansa, come o hace popó, permanece en la misma parcela
> 
> El juego termina una vez que la vaca hace popó
