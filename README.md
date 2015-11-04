# CHUK - Companies House UK - Python Client

This is a beta client for the [Companies House](https://www.gov.uk/government/organisations/companies-house) Beta Api.

Compatible with Python 2 and 3. No dependencies required.

More documentation to come, but a simple usage:

```python
>>> from chuk import CompanyHouseAPI
>>> api = CompanyHouseAPI(key="11bbccdd")
>>> response = api.company_profile("08861249")
>>> print response.code
200
>>> print response.data # https://developer.companieshouse.gov.uk/api/docs/company/company_number/companyProfile-resource.html
{u'accounts': [...]}
```
