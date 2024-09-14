from jaeger_client import Config

def init_tracer(service_name: str):
    config = Config(config={"sampler": {"type": "const", "param": 1},
                            "logging": True},
                    service_name=service_name)
    return config.initialize_tracer()
