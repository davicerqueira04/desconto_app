from src.app.framework.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController

    
if __name__ == "__main__":
    database = MemoryDatabase()
    repo = MemoryPedidoRepository(database)
    criar_pedido = CriarPedido(pedido_gateway)
    controller = PedidoController(criar_pedido_use_case)

    pedido1 = Pedido("Cliente 1", DescontoNormal())
    pedido1.valor_original = 100.0
    pedido2 = Pedido("Cliente 2", DescontoVIP())
    pedido2.valor_original = 100.0
    pedido3 = Pedido("Cliente 3", DescontoPremium())
    pedido3.valor_original = 100.0

    controller.criar_pedido("Cliente 1", 100.0, "normal")
    controller.criar_pedido("Cliente 2", 100.0, "vip")
    controller.criar_pedido("Cliente 3", 100.0, "premium")

    controller.listar_pedidos()