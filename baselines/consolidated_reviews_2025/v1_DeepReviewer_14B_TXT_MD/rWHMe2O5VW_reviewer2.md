### Summary

This paper proposes a method called PGODE, which is the first to connect context mining with a prototypical graph ODE approach for modeling challenging interacting dynamics. The method extracts hierarchical contexts with representation disentanglement and system parameters, which are then integrated into a graph ODE model that utilizes prototype decomposition. Extensive experiments validate the efficacy of PGODE in different challenging settings.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

1. The problem studied in this paper is very important in the field of graph representation learning. 
2. The proposed PGODE is the first to connect context mining with a prototypical graph ODE approach for modeling challenging interacting dynamics. 
3. Extensive experiments validate the efficacy of PGODE in different challenging settings.

### Weaknesses

#### Some Related Works


#### comment

1. The paper proposes to extract hierarchical contexts with representation disentanglement and system parameters. However, the paper does not explain the specific implementation of representation disentanglement. 
2. The paper does not explain the specific implementation of capturing contexts from system parameters.
3. The paper does not explain how to determine the number of prototypes.
4. The paper does not explain the specific implementation of the graph ODE framework.
5. The paper does not explain how to capture long-term dynamics through continuous evolution instead of discrete rollouts in detail.

### Suggestions

The paper introduces a novel approach, PGODE, for modeling interacting dynamics using a prototypical graph ODE framework. However, several key implementation details are lacking, hindering a full understanding and potential reproducibility of the method. Specifically, the paper needs to elaborate on the representation disentanglement process. While the idea of separating object-level and system-level contexts is promising, the paper does not provide sufficient detail on how this is achieved. For instance, what specific loss functions are used to enforce disentanglement? How are the object-level and system-level embeddings initialized and updated during training? What is the dimensionality of these embeddings, and how does this affect the model's capacity to capture complex interactions? Without these details, it is difficult to assess the effectiveness of the disentanglement strategy and its impact on the overall performance of PGODE. Furthermore, the paper should clarify how the system parameters are incorporated into the model. It is mentioned that these parameters are used to capture system-level contexts, but the exact mechanism is not described. Are these parameters directly fed into the graph ODE model, or are they first processed through an embedding layer? How does the model handle varying numbers of system parameters across different datasets? Providing these details would significantly improve the clarity and reproducibility of the proposed method.

Another area that requires further clarification is the prototype decomposition mechanism. The paper mentions that PGODE learns a set of GNN prototypes to characterize the entire GNN space, but it does not explain how these prototypes are initialized, trained, and selected during the dynamic process. What is the architecture of these GNN prototypes? How are the weights for each prototype determined? The paper also needs to specify how the number of prototypes is determined. Is this a hyperparameter that is tuned through cross-validation, or is there a more principled approach? Without a clear explanation of the prototype decomposition process, it is difficult to understand how PGODE captures the diverse interaction patterns in the data. Moreover, the paper should provide more details on the graph ODE framework. While the paper mentions that it uses a continuous graph ODE framework, it does not specify the exact form of the ODE solver used. Is it a first-order Euler method, or a higher-order method like Runge-Kutta? How is the time step size chosen? What are the specific equations that govern the evolution of the node embeddings over time? Providing these details would allow readers to better understand the continuous dynamics modeling aspect of PGODE.

Finally, the paper needs to elaborate on how PGODE captures long-term dynamics through continuous evolution instead of discrete rollouts. While the use of a continuous graph ODE framework is mentioned, the paper does not explain how this approach avoids error accumulation over long prediction horizons. How does the continuous evolution ensure numerical stability? How does the model handle potential stiffness in the ODE system? Providing a more detailed explanation of these aspects would strengthen the paper's claims about the advantages of PGODE for long-term dynamics modeling. In addition, the paper should include a more thorough discussion of the limitations of the proposed method and potential directions for future research. This would provide a more balanced perspective on the contributions of PGODE and its place within the broader field of graph-based dynamical systems modeling.

### Questions

Please see the weakness.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
