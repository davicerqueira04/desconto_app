from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.presenters.pedido_presenter import PedidoPresenter

    
if __name__ == "__main__":
    database = MemoryDatabase()
    repo = MemoryPedidoRepository(database)
    criar_pedido = CriarPedido(repo)
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido, presenter)

    print(controller.criar_pedido("Cliente 1", 100.0, "normal"))
    print(controller.criar_pedido("Cliente 2", 100.0, "vip"))
    print(controller.criar_pedido("Cliente 3", 100.0, "premium"))

    print("Pedidos cadastrados:")
    for pedido in controller.listar_pedidos():
        print(pedido)
