from .inventory_service import InventoryService
from .notification_service import NotificationService
from .order import Order
from .order_fulfillment_facade import OrderFulfillmentFacade
from .payment_service import PaymentService
from .shipping_service import ShippingService


class OrderClient:
    def __init__(self, inventory: InventoryService, payment: PaymentService, shipping: ShippingService, notification: NotificationService):
        self.facade = OrderFulfillmentFacade(inventory, payment, shipping, notification)

    def place_order(self, order: Order) -> list[str]:
        return self.facade.place_order(order)
