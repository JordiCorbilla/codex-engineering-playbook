export type OrderSummary = {
  id: string;
  customerName: string;
  totalAmount: number;
};

export type ApiError = {
  message: string;
  status: number;
};

export async function fetchOrders(signal?: AbortSignal): Promise<OrderSummary[]> {
  const response = await fetch("/api/orders", { signal });

  if (!response.ok) {
    const message = await response.text();
    throw {
      message: message || "Request failed.",
      status: response.status,
    } satisfies ApiError;
  }

  return (await response.json()) as OrderSummary[];
}
