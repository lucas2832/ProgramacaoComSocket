#Programação com Socket

##Trabalho prático da disciplina de Redes de Computadores II

###Autor
- Lucas Martins da Silva Cruz

###Sobre o trabalho:
  Quando se inicia a interação cliente servidor, é definido um limite de interações para
 negociação. Neste trabalho existem dois loops de interação. O primeiro loop é apenas para
 garantir que o usuário insira corretamente o código de algum produto existente na loja. O
 segundo loop é destinado a negociação, que possui um limite preestabelecido.
   Odesconto máximo é de 30%, ou seja, se o usuário enviar um valor abaixo de 70% do
 preço original do produto, o servidor recusa a oferta e envia uma contraproposta. Para a
 contraproposta, o servidor sorteia um desconto de 2% a 5% e envia ao usuário, como uma
 sugestão. Caso o usuário envie uma proposta acima de 70% do valor original, o servidor
 confirma a compra e a interação é encerrada. Mas se exceder o número de tentativas, o
 servidor avisa ao usuário que o limite foi excedido e que não será possível concluir a
 compra. Logo em seguida a conexão é encerrada.

 ###Instruções de uso:
- No campo 'serverName', insira o endereço ip do dispositivo que será o servidor nessa interação. Ou mantenha "localhost", caso a toda interação aconteça no mesmo dispositivo.
- Na IDE de sua preferência, inicie primeiramente o servidor e, em seguida, o cliente. O cliente irá iniciar a interação automaticamente. Após isso, siga as instruções passadas pelo servidor.
