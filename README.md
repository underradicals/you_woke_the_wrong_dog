# You_Woke_The_Wrong_Dog

## Download Function


### Part 0
- Need the following information
  - URL: str
  - Destination-Path: str


### Part 1
- Send HEAD Request
- Check Store for ETag or Last-Modified Values
- Create .part file
- Create Metadata file (JSON)
- Parse Headers
  - ETAG
  - Last-Modified
  - Content-Length
  - Accept-Ranges
  - Transfer-Encoding
- If Metada file exist then compare existing data with the data in the requested headers.
  - If different: file has changed → delete partial and metadata.
  - If same: proceed to resume.
- If only partial file exists without metadata:
  - Unsafe to resume → delete partial file.
- Perform a conditional GET using If-None-Match or If-Modified-Since.
  - f server returns 304 Not Modified Skip download.
  - If server returns 200 OK: File is outdated → proceed with full re-download.