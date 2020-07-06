#!/usr/bin/env python3
from kpTranslator.config import connex_app

def main():
  connex_app.add_api('openapi.yaml',
            arguments={'title': 'OpenAPI for NCATS Biomedical Translator Reasoners'},
            pythonic_params=True)
  connex_app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
  main()