from dls_toolkit import aws


def test_get_last_n_months_date_range():
    start_date, end_date = aws.get_last_n_months_date_range(4)
    print(f"start_date: {start_date}")
    print(f"end_date: {end_date}")


    for a in aws.get_monthly_bill_amount(4, "750213756132"):
        print(a)
        print()
    assert False