import time
def rate_limit(max_calls: int, period: float):

    def decorator(func):
        call_history = []

        def wrapper(*args, **kwargs):
            current_time = time.time()
            nonlocal call_history
            call_history = [t for t in call_history if current_time - t < period]

            if len(call_history) >= max_calls:
                oldest_call = call_history[0]
                wait_time = period - (current_time - oldest_call)

                if wait_time > 0:
                    time.sleep(wait_time)
                    current_time = time.time()
                    call_history = [t for t in call_history if current_time - t < period]
                    
            call_history.append(current_time)
            call_history = call_history[-max_calls:]

            return func(*args, **kwargs)
            
        return wrapper
        
    return decorator