# Assigment 1

## Setting

-   setting on file `.env`

    ```.env
    API_KEY=my-api-key
    API_SECRET=my-api-secret
    ```

## Run Script
- Create Sell Order

    ```bash
    python3 create_sell_order.py symbol amount rate order_type
    ```
- Create Buy Order 

    ```bash
    python3 create_buy_order.py symbol amount rate order_type
    ```
- Cancel Order

    ```bash
    python3 cancel_order.py symbol order_id order_side
    ```
