def greet(name):
    return (f"Hello, {name}!")
    def process_name(name, callback):
        modified_name = name.strip().title()
        return callback(modified_name)
        process_name("zero",greet)