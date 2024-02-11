
from dls_toolkit import aws

def test_scratch():
    aid = "750213756132"
    amounts = list(aws.get_monthly_bill_amount(4, aid))
    print(amounts)
    assert False