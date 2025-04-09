# Fetch Spec

## Signatue

#### Arguments
- url [str] 
  - The partial url (The base url is defined in the AsyncClient)
- cache_prefix [str]
  - The string prefix to prepend to the cache_key
- max_retries [int]
  - The number of times the method should attempt to retry before failing
- retry_delay [float]
  - The delay before the method shoul make another attempt


### Steps
- local

cache_key
meta_key

- Check for current metadata
- Create headers
- Check for Last Modified Header
- Check for ETag

