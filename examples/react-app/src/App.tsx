import { useState } from "react";

import { OrderSummaryList } from "./components/OrderSummaryList";
import { StatusPanel } from "./components/StatusPanel";
import { useOrders } from "./hooks/useOrders";

export function App() {
  const [scenario, setScenario] = useState<"ready" | "empty" | "error">("ready");
  const state = useOrders(scenario);

  return (
    <main className="app-shell">
      <section className="hero">
        <p className="eyebrow">React + TypeScript Example</p>
        <h1>Order queue with explicit async UI states</h1>
        <p className="hero-copy">
          This example keeps the API client separate from rendering, uses a small hook for state
          transitions, and makes loading, empty, and error paths first-class UI states.
        </p>
      </section>

      <section className="toolbar" aria-label="Demo scenario">
        <button
          className={scenario === "ready" ? "active" : ""}
          onClick={() => setScenario("ready")}
          type="button"
        >
          Populated
        </button>
        <button
          className={scenario === "empty" ? "active" : ""}
          onClick={() => setScenario("empty")}
          type="button"
        >
          Empty
        </button>
        <button
          className={scenario === "error" ? "active" : ""}
          onClick={() => setScenario("error")}
          type="button"
        >
          Error
        </button>
      </section>

      <StatusPanel title="Orders">
        {state.kind === "loading" ? <p>Loading orders...</p> : null}
        {state.kind === "error" ? <p role="alert">{state.message}</p> : null}
        {state.kind === "empty" ? <p>No orders are waiting for review.</p> : null}
        {state.kind === "ready" ? <OrderSummaryList orders={state.orders} /> : null}
      </StatusPanel>
    </main>
  );
}
