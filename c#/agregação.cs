 public class Pedido{
     
        // um objeto pode compor outros objetos 
        //com suas propriedades
        public Cliente Cliente { get; set; }
        public Endereco EnderecoPostagem { get; set; }
        public List<PedidoItem> Pedidos { get; set; }
    }