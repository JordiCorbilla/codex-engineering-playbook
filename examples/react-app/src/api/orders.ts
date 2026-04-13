export type OrderSummary = {
  id: string;
  customerName: string;
  status: "Pending" | "Approved" | "Escalated";
  totalAmount: number;
};

const seededOrders: OrderSummary[] = [
  { id: "ord-102", customerName: "Northwind", status: "Pending", totalAmount: 1840.5 },
  { id: "ord-103", customerName: "Acme Corp", status: "Escalated", totalAmount: 4212.0 },
  { id: "ord-104", customerName: "Fabrikam", status: "Approved", totalAmount: 715.2 },
];

export async function listOrders(
  scenario: "ready" | "empty" | "error",
  signal?: AbortSignal,
): Promise<OrderSummary[]> {
  await new Promise<void>((resolve, reject) => {
    const timeout = window.setTimeout(resolve, 250);
    signal?.addEventListener(
      "abort",
      () => {
        window.clearTimeout(timeout);
        reject(new DOMException("Request aborted", "AbortError"));
      },
      { once: true },
    );
  });

  if (scenario === "error") {
    throw new Error("The order service is temporarily unavailable.");
  }

  return scenario === "empty" ? [] : seededOrders;
}
