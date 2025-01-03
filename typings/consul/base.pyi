from typing import Any, Dict, List, Optional, Tuple
class ConsulException(Exception): ...
class NotFound(ConsulException): ...
class Consul:
    http: Any
    agent: 'Consul.Agent'
    session: 'Consul.Session'
    kv: 'Consul.KV'
    class KV:
        def get(self, key: str, index: Optional[int]=None, recurse: bool = False, wait: Optional[str] = None, token: Optional[str] = None, consistency: Optional[str] = None, keys: bool = False, separator: Optional[str] = '', dc: Optional[str] = None) -> Tuple[int, Dict[str, Any]]: ...
        def put(self, key: str, value: str, cas: Optional[int] = None, flags: Optional[int] = None, acquire: Optional[str] = None, release: Optional[str] = None, token: Optional[str] = None, dc: Optional[str] = None) -> bool: ...
        def delete(self, key: str, recurse: Optional[bool] = None, cas: Optional[int] = None, token: Optional[str] = None, dc: Optional[str] = None) -> bool: ...
     class Agent:
        service: 'Consul.Agent.Service'
        def self(self) -> Dict[str, Dict[str, Any]]: ...
        class Service:
            def register(self, name: str, service_id=..., address=..., port=..., tags=..., check=..., token=..., script=..., interval=..., ttl=..., http=..., timeout=..., enable_tag_override=...) -> bool: ...
            def deregister(self, service_id: str) -> bool: ...
    class Session:
        def create(self, name: Optional[str] = None, node: Optional[str] = [], checks: Optional[List[str]]=None, lock_delay: float = 15, behavior: str = 'release', ttl: Optional[int] = None, dc: Optional[str] = None) -> str: ...
        def renew(self, session_id: str, dc: Optional[str] = None) -> Optional[str]: ...
