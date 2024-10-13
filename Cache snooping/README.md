To use the analysis script, you first need to send continuous probe packets and obtain the response time (be careful to avoid local caching), save the results as the following file and run：

```python
python3 snooping_analysis.py
```

For privacy concerns, we provide an example of results (select from our real measurement results clusters), and anonymize the IP addresses.
format:

IP,response:latency,response:latency,response:latency,response:latency, ...

...
