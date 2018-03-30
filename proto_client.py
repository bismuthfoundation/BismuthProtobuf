# A stripped down Bismuth node client - For connection benchmark only
# Protobuf protocol version with abstraction layer

import json
import comhandler
import commands_pb2

version = "posnet0001"


# PORT = 6568 #6568 for legacy protocol, 6569 is the server running the protobuff protocol

peer = {}
peer['127.0.0.1'] = 6569
print(peer)
for ip, port in peer.items():
    print(ip, port)

# This client can talk to both
# PROTOCOL_VERSION = comhandler.VER_LEGACY
PROTOCOL_VERSION = comhandler.VER_PROTO

if __name__ == "__main__":

    handler = comhandler.Connection (version=PROTOCOL_VERSION)
    print ("Handler", handler.status ())

    try:
        print ("Connecting to", ip, port)


        handler.connect (ip, port)
        print ("Handler", handler.status ())
        # communication starter

        handler.send_string (commands_pb2.Command.version, version)

        print ("Handler", handler.status ())

        message = handler.get_message ()

        print ("Got message", message.__str__ ())
        print ("Handler", handler.status ())

        if (message.command == commands_pb2.Command.ok):
            print ("Outbound: Node protocol version of {} matches our client".format (ip))
        else:
            raise ValueError ("Outbound: Node protocol version of {} mismatch".format (ip))


    except Exception as e:
        print ("Could not connect to {}: {}".format (ip, port), e)


