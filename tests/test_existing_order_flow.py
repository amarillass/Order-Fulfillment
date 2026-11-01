from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order import Order
from order_fulfillment.order_client import OrderClient
from order_fulfillment.order_fulfillment_facade import OrderFulfillmentFacade
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService


def test_client_places_order_through_facade():
    facade = OrderFulfillmentFacade(
        InventoryService(), PaymentService(), ShippingService(), NotificationService()
    )
    client = OrderClient(facade)
    order = Order("O-1", "SKU-9", 125.0, "Guadalajara")

    steps = client.place_order(order)

    assert steps == [
        "inventory:reserved:SKU-9",
        "payment:charged:125.00",
        "shipping:created:Guadalajara",
        "notification:sent:O-1",
    ]
