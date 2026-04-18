create schema if not exists analytics;

create or replace table analytics.partner_sales_daily (
    partner_id varchar,
    country varchar,
    sale_date date,
    daily_sales_amount number(18, 2),
    sales_band varchar,
    load_timestamp timestamp_ntz
);
