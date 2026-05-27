import pandas as pd

from sklearn.linear_model import LinearRegression

# ==================================================
# SALES FORECAST
# ==================================================

def generate_sales_forecast(

    sales_df,
    periods=6

):

    # ==================================================
    # PREP DATA
    # ==================================================

    df = sales_df.copy()

    df = df.sort_values(

        ["year", "month"]

    )

    df["period_index"] = range(

        len(df)

    )

    # ==================================================
    # TRAIN MODEL
    # ==================================================

    X = df[["period_index"]]

    y = df["venta_total"]

    model = LinearRegression()

    model.fit(

        X,
        y

    )

    # ==================================================
    # FUTURE PERIODS
    # ==================================================

    future_indexes = list(

        range(

            len(df),
            len(df) + periods

        )

    )

    future_df = pd.DataFrame({

        "period_index": future_indexes

    })

    # ==================================================
    # PREDICT
    # ==================================================

    future_df["forecast_sales"] = model.predict(

        future_df[["period_index"]]

    )

    # ==================================================
    # FORECAST PERIOD LABELS
    # ==================================================

    last_year = int(

        df.iloc[-1]["year"]

    )

    last_month = int(

        df.iloc[-1]["month"]

    )

    periods_labels = []

    current_year = last_year

    current_month = last_month

    for _ in range(periods):

        current_month += 1

        if current_month > 12:

            current_month = 1

            current_year += 1

        periods_labels.append(

            f"{current_year}-{current_month}"

        )

    future_df["periodo"] = periods_labels

    # ==================================================
    # RESULT
    # ==================================================

    return future_df[
        [

            "periodo",
            "forecast_sales"

        ]
    ]