import { useEffect, useState } from "react";

import { fetchOrders, type OrderSummary } from "./api-client";

type LoadableOrders =
  | { kind: "loading" }
  | { kind: "error"; message: string }
  | { kind: "empty" }
  | { kind: "ready"; orders: OrderSummary[] };

export function OrdersPanel() {
  const [state, setState] = useState<LoadableOrders>({ kind: "loading" });

  useEffect(() => {
    const controller = new AbortController();

    void fetchOrders(controller.signal)
      .then((orders) => {
        setState(orders.length === 0 ? { kind: "empty" } : { kind: "ready", orders });
      })
      .catch((error: { message?: string }) => {
        if (controller.signal.aborted) {
          return;
        }

        setState({ kind: "error", message: error.message ?? "Could not load orders." });
      });

    return () => controller.abort();
  }, []);

  if (state.kind === "loading") {
    return <p>Loading orders...</p>;
  }

  if (state.kind === "error") {
    return <p role="alert">{state.message}</p>;
  }

  if (state.kind === "empty") {
    return <p>No orders yet.</p>;
  }

  return (
    <ul>
      {state.orders.map((order) => (
        <li key={order.id}>
          {order.customerName}: ${order.totalAmount.toFixed(2)}
        </li>
      ))}
    </ul>
  );
}
