import paypalrestsdk
import logging

logging.basicConfig(level=logging.INFO)

paypalrestsdk.configure({
    "mode": "sandbox",  # sandbox or live
    "client_id": "AfWJWvkI5DV4M1vgS3xbpkDbI8IP-0Xo6OglRor32voNWWDJ9bu5SBZ5UYf5Oy42LCO6ym81XjUdf3N1",
    "client_secret": "EL9ak3plo5d_0qtQJ72KxkFwSJRTVgrkP45dwLIFnqwV5D98SkIgLyTPuer9oBmF9OMyaCexkRpa0vPv"
})
