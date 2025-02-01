"""
library financial structure and viability radio :
+modul :
    + capitalallocation
    +class : capital_structure:
        + args:[
            + active:float=1.0,
            + fixed:float=1.0,
            + current_assets:float=1.0,
            + liabilities :float=1.0,
            + self_foreign :float=1.0,
            + short_term_foreign_funds :float=1.0,
            + long_term_foreign_capital:float=1.0,
            + interest_rate:float = 0.1,
            + incom_tax:float = 1.0,
            + tax_rate:float = 1.0
            ]
        +method :
            +foreign_capital_ratio_calculation -> (float | None)\n
            +total_capital -> (float | None)\n
            +leverage_tax_reduction -> (str | None)\n
            +distribution_of_assets -> (Literal['low liquidity of assets', 'balance', 'High liquidity of assets'] | None)\n
            +radio_of_owners_equity_to_total_assets-> str\n
            +foreign_capital_pressure_index-> str\n
            +radio_of_owners_equity_to_total_liavilities -> str\n
            +listed_radio_of_owners_equity_to_total_liavilities->str\n
            +asset_structure_radio->str\n
            +radio_of_owners_qquity_to_fixed_assets-> float\n
"""

