import { render, screen } from "@testing-library/react";

import { OrderSummaryList } from "./OrderSummaryList";

describe("OrderSummaryList", () => {
  it("renders typed order data", () => {
    render(
      <OrderSummaryList
        orders={[
          {
            id: "ord-1",
            customerName: "Acme Corp",
            status: "Pending",
            totalAmount: 12.5,
          },
        ]}
      />,
    );

    expect(screen.getByText("Acme Corp")).toBeInTheDocument();
    expect(screen.getByText("Pending")).toBeInTheDocument();
    expect(screen.getByText("$12.50")).toBeInTheDocument();
  });
});
