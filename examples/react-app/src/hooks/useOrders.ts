import { useEffect, useState } from "react";

import { listOrders, type OrderSummary } from "../api/orders";

type OrdersState =
  | { kind: "loading" }
  | { kind: "error"; message: string }
  | { kind: "empty" }
  | { kind: "ready"; orders: OrderSummary[] };

export function useOrders(scenario: "ready" | "empty" | "error"): OrdersState {
  const [state, setState] = useState<OrdersState>({ kind: "loading" });

  useEffect(() => {
    const controller = new AbortController();

    setState({ kind: "loading" });

    void listOrders(scenario, controller.signal)
      .then((orders) => {
        if (orders.length === 0) {
          setState({ kind: "empty" });
          return;
        }

        setState({ kind: "ready", orders });
      })
      .catch((error: unknown) => {
        if (controller.signal.aborted) {
          return;
        }

        setState({
          kind: "error",
          message: error instanceof Error ? error.message : "Could not load orders.",
        });
      });

    return () => controller.abort();
  }, [scenario]);

  return state;
}
