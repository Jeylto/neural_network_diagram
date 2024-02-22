from graphviz import Digraph

def create_neural_graph(input_layers, hidden_neurons, output_layers):
    # Create a new Digraph object
    dot = Digraph()

    # Define the graph style
    dot.attr(rankdir='LR')
    dot.attr(splines='line')

    # Define the style of nodes to be empty
    dot.attr('node', fixedsize='true', label='')

    # Define the nodes and group them into clusters for input layers
    with dot.subgraph(name='cluster_0') as c:
        c.attr(color='white')
        c.attr('node', style='solid', color='blue4', shape='circle')
        for i in range(input_layers):
            c.node(f'x{i+1}')
        c.attr(label='layer 1 (Input layer)')

    # Define the nodes and group them into clusters for hidden layers
    for j in range(len(hidden_neurons)):
        with dot.subgraph(name=f'cluster_{j+1}') as c:
            c.attr(color='white')
            c.attr('node', style='solid', color='red2', shape='circle')
            for k in range(hidden_neurons[j]):
                c.node(f'a{j+1}{k+1}')
            c.attr(label=f'layer {j+2} (hidden layer)')

    # Define the nodes and group them into clusters for output layers
    with dot.subgraph(name=f'cluster_{len(hidden_neurons)+1}') as c:
        c.attr(color='white')
        c.attr('node', style='solid', color='seagreen2', shape='circle')
        for m in range(output_layers):
            c.node(f'O{m+1}')
        c.attr(label='layer {0} (output layer)'.format(len(hidden_neurons)+2))

    # Define the connections between the nodes
    # Connections from input layers to hidden layers
    for i in range(input_layers):
        for j in range(hidden_neurons[0]):
            dot.edge(f'x{i+1}', f'a1{j+1}')

    # Connections between hidden layers
    for i in range(len(hidden_neurons) - 1):
        for j in range(hidden_neurons[i]):
            for k in range(hidden_neurons[i+1]):
                dot.edge(f'a{i+1}{j+1}', f'a{i+2}{k+1}')

    # Connections from hidden layers to output layer
    for j in range(hidden_neurons[-1]):
        for k in range(output_layers):
            dot.edge(f'a{len(hidden_neurons)}{j+1}', f'O{k+1}')

    # Render the graph
    dot.render('graph', format='png', cleanup=True)

# Usage example:
input_layers = 4 # Number of neurons in input layer
hidden_neurons = [10, 10, 10]  # Number of neurons in each hidden layer
output_layers = 4 # Number of neurons in output layer

create_neural_graph(input_layers, hidden_neurons, output_layers)
