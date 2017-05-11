Channels extends Django to add a new layer that allows two important features:

WebSocket handling, in a way very similar to normal views
Background tasks, running in the same servers as the rest of Django
It allows other things too, but these are the ones you’ll use to start with. Django responds to a wide array of events sent on channels. There’s still no persistent state - each event handler, or consumer as we call them, is called independently in a way much like a view is called.

What is a channel?
It is an ordered, first-in first-out queue with message expiry and at-most-once delivery to only one listener at a time.

How?
It separates Django into two process types:

One that handles HTTP and WebSockets
One that runs views, websocket handlers and background tasks (consumers)
They communicate via a protocol called ASGI, which is similar to WSGI but runs over a network and allows for more protocol types.

Channels does not introduce asyncio, gevent, or any other async code to your Django code; all of your business logic runs synchronously in a worker process or thread.

What else does Channels give me?
Other features include:

Easy HTTP long-poll support for thousands of clients at once
Full session and auth support for WebSockets
Automatic user login for WebSockets based on site cookies
Built-in primitives for mass triggering of events (chat, live blogs, etc.)
Zero-downtime deployment with browsers paused while new workers spin up
Optional low-level HTTP control on a per-URL basis
Extendability to other protocols or event sources (e.g. WebRTC, raw UDP, SMS)


Reference:
http://channels.readthedocs.io/en/latest/reference.html
