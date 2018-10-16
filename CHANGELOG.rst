Changelog
---------

1.2.0
++++++++++++++++++
- Send to STDOUT the output from apidoc #12.

1.1.2
++++++++++++++++++
- Fix: apidoc.json without a url was raising an error.

1.1.1
++++++++++++++++++
- Fix: Open files using utf-8 encoding, this prevent errors like "UnicodeDecodeError: 'ascii' codec can't decode."

1.1.0
++++++++++++++++++
- Add support for absolute url in @api

1.0.0
++++++++++++++++++
- Add support to Python 2.7 (:issue:`1`). Thanks :user:`hellking4u`.
- Add ``dynamic_url`` parameter to enabled/disable dynamic urls in ApiDoc files.
