# Server-Client Field Trap Process



# Work Flow:

```mermaid
  flowchart TB
    subgraph Set-Up
        direction TB
        id1([Power Pi Wifi Hub]) --> id2([Sever Start Up on Laptop])

        end

    subgraph Pi Nodes 
        direction TB
        id2([Sever Start Up on Laptop]) --> id3([Power Pi Nodes])
        
        id3([Power Pi Nodes]) --> id4([Clients Connect To Server])
        end

    subgraph Server Functionality
        direction RL
        id4([Clients Connect To Server]) --> id5([Server Recieves Confirmation of Client Connection])
        id5([Server Recieves Confirmation of Client Connection]) --> id6([User Runs One of Three Commands])
        end
    subgraph Server Commands
        id6([User Runs One of Three Commands])-->id7(["Check Image"])
        id6([User Runs One of Three Commands])-->id8(["Run Experiment"])
        id6([User Runs One of Three Commands])-->id10(["Kill Process"])
        end