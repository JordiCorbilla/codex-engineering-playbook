import type { OrderSummary } from "../api/orders";

type OrderSummaryListProps = {
  orders: OrderSummary[];
};

export function OrderSummaryList({ orders }: OrderSummaryListProps) {
  return (
    <ul className="order-list">
      {orders.map((order) => (
        <li className="order-card" key={order.id}>
          <div>
            <p className="order-card__customer">{order.customerName}</p>
            <p className="order-card__id">{order.id}</p>
          </div>
          <div className="order-card__meta">
            <span className={`pill pill--${order.status.toLowerCase()}`}>{order.status}</span>
            <strong>${order.totalAmount.toFixed(2)}</strong>
          </div>
        </li>
      ))}
    </ul>
  );
}
