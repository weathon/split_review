# Personalized Federated Learning via Tailored Lorentz Space

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 6, 6, 6, 3

## Abstract
Personalized Federated Learning (PFL) has gained attention for privacy-preserving training on heterogeneous data. However, existing methods fail to capture the unique inherent geometric properties across diverse datasets by assuming a unified Euclidean space for all data distributions. Drawing on hyperbolic geometry's ability to fit complex data properties, we present FlatLand, a novel personalized federated learning method that embeds different clients' data in tailored Lorentz space. FlatLand can directly tackle the challenge of heterogeneity through the personalized curvatures of their respective Lorentz model of hyperbolic geometry, which is manifested by the time-like dimension. Leveraging the Lorentz model properties, we further design a parameter decoupling strategy that enables direct server aggregation of common client information, with reduced heterogeneity interference and without the need for client-wise similarity estimation. To the best of our knowledge, this is the first attempt to incorporate Lorentz geometry into personalized federated learning. Empirical results on various federated graph learning tasks demonstrate that FlatLand achieves superior performance, particularly in low-dimensional settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new personalized federated learning algorithm called Flatland employing hyperbolic geometry. One of the key challenges in federated learning is the data heterogeneity among clients and understanding the similarity between clients data distributions can be helpful. The paper tries to achieve this goal by projecting each client data to a higher dimension to better capture similarities between clients data. The paper more focused on graph data. Experiments are carried out to showcase the effectiveness of the approach.

### Strengths
- The motivation and contribution of the paper is clear and it seems that leveraging hyperbolic geometric approaches can be helpful for personalized federated learning.
- The paper provides analysis in Section 6 to support their approach.
- Experimental study of the paper looks convincing.

### Weaknesses
Reading of the paper, I felt that some arguments in the paper are vague and needs more explanations to become more clear. For example "*PFL approaches include segmenting models into generic and personalized components (McMahan et al., 2017; Tan et al., 2023), leveraging model weights and gradients to map client relationships (Xie et al., 2021), or integrating additional modules to facilitate customization (Baek et al., 2023)*." Or for example in "Moreover, embedding data from various clients into a fixed space complicates the interpretability of model parameters, making it difficult to segment the model into meaningful components (Arivazhagan et al., 2019) and often expensive to assess similarities between client models", the reasons are not clear.

Furthermore, the paper states that embedding data from various clients into a fixed space often expensive to assess similarities between client models. However, using the Flatland itself in step 4 of algorithm 2, each clients needs to project its data to another space. I believe this can add more computations compared to other methods which does not employ Lorentz space and hyperbolic geometry-based approaches. Therefore, to me the above argument seems a bit contradictory.

### Questions
Looking into algorithm 2 of the paper, it seems that using Flatland clients and the server collaborate using conventional federated averaging methods such as Fedavg. Is Flatland compatible with other personalized federated learning algorithms? Is it possible to use other methods like PerFedAvg to orchestrate the collaboration between the server and clients? Maybe this can further improve personalization properties of Flatland.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper studies the federated graph learning problem, and proposes to model data heterogeneity across different clients as different Lorentz spaces with different curvatures. The authors adapt the Lorentz network into the FL framework, and propose to maintain dedicated trainable client-specific parameters to learn different client curvatures, which makes the new method FlatLand different from previous baselines. Simulation results and ablation studies are also presented in the paper to support the better performance of the new method.

### Strengths
Although there are already many works on federated hyperbolic learning, I found the idea in this paper still interesting and inspiring. The proposed method is concise yet intuitive, and the simulation results seem to suggest that it also works well in practice for graph-related problems.

### Weaknesses
The presentation of this paper can be improved. 

- Firstly, some of the notations are not consistent in the paper and can make readers confusing. For example, line 286-290, if $x^{(l)}$ is in $\mathcal{L}^n_K$, then it should be explicitly stated that the spatial component $x_s^{(l)}$ belongs to $\mathbb{R}^n$ instead of $\mathbb{R}^d$. Similarly, the dimensions of $m^{(l)}$ and $M^{(l)}$ should be clearly defined as $\mathbb{R}^{m}$ and $\mathbb{R}^{m\times n}$, respectively, to avoid ambiguity. This type of inconsistency exists throughout the paper and needs to be rectified for clarity.

- Secondly, some of the statements in the paper are left unexplained, which makes me very confused. For example, in lines 167-168, the authors state "For instance, for dropout, the operation function is f(Wx, v) = W dropout (x).", but the role of the bias term 'v' is not clarified in this context. It is unclear how 'v' is incorporated into the dropout operation or if it is utilized at all. Another example is Equation (4), where it appears that the first row of $\hat{M}^{(l)}$ is not used in each LT layer. The authors should clarify the purpose of this first row and whether any components are intentionally omitted. Furthermore, the paper should explicitly state that $K$ is a learnable scalar representing the curvature.

- Thirdly, the application of the proposed method to solve the federated **graph** learning problem is not clearly explained in the main text. While the method is presented as suitable for transforming node features, its applicability to the adjacency matrix is not discussed. This creates confusion when the authors directly apply the method to graph datasets in the simulation section. In the appendix, it is mentioned that "For the node classification task, we employ 2-layer GCN for Euclidean models, 2-layer LGCN Chen et al. (2021) for FlatLand... For graph classification, we use 3-layer GIN Xu et al. (2018) as the Euclidean encoder, and the same 3-layer hyperbolic encoders as node classification for hyperbolic models". However, it is unclear how LGCN is integrated with the proposed method and what precisely constitutes the "3-layer hyperbolic encoders." The authors should provide a detailed explanation of these details in the main text, including a clear description of how the Lorentz transformations are combined with graph aggregation operations. A pseudocode representation of the algorithm would also significantly enhance clarity.

- Lastly, I find that the authors provide the implementation of the method with a text link in the doc (line 404, "anonymous repository") instead of uploading it as a supplementary file. I nearly missed it. I would recommend the authors to upload the code directly whenever possible.

### Questions
1. Is the parameter $K$ in equation (4) just a learnable scalar? Do we need to have any kind of regularization/restrictions on $K$?

2. Line 501, what does "no parameter decoupling strategy" mean? Does it mean the server will aggregate all parameters including the client-learned curvatures?

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new personalized federated learning approach called FlatLand. Unlike current methods that commonly operate in Euclidean space, FlatLand embeds client data in a Tailored Lorentz space to more effectively represent the clients’ data distributions. Building on this foundation, the authors introduce a parameter decoupling strategy to aggregate shared parameters efficiently. Extensive experiments demonstrate the effectiveness of FlatLand.

### Strengths
1. The paper is well-written and easy to follow. 
2. The idea of increasing dimensionality to embed client data in Lorentz space is novel.
3. Experiments are extensive.

### Weaknesses
1. Techniques that personalize client models by creating localized models or layers are highly relevant to this paper. However, the related work section includes somewhat outdated references. It would benefit from incorporating more recent approaches, such as FedCAC [1] and GPFL [2]. Additionally, the experiments lack comparisons with these types of methods.

2. This paper primarily focuses on graph datasets. Can FlatLand effectively perform on commonly used benchmarks in PFL, such as CV datasets (e.g., CIFAR-100) and text datasets (e.g., AGNEWS)?

### Questions
Please see the weaknesses above.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces FlatLand, a novel personalized federated learning (PFL) approach that addresses data heterogeneity across clients by leveraging hyperbolic geometry, specifically Lorentz space. Unlike traditional PFL methods that operate in Euclidean space, FlatLand embeds each client's data in a tailored Lorentz space with different curvatures to better capture non-Euclidean properties of the data. Instead of explicitly calculating client similarities or using additional modules for personalization, FlatLand leverages the geometric properties of Lorentz space to handle heterogeneity naturally through different curvatures. Also, they use parameter decoupling for shared and local models, similar to some other personalized FL models.

### Strengths
This paper presents an innovative approach to personalized federated learning by leveraging hyperbolic geometry, specifically through the use of Lorentz spaces with tailored curvatures for different clients. The theoretical foundation is well-developed, with mathematical proofs and insights connecting geometric properties to data heterogeneity. The experimental results show promising improvements over existing methods, particularly in low-dimensional settings, which could be valuable for resource-constrained environments. The parameter decoupling strategy based on geometric properties is elegant and eliminates the need for explicit client similarity calculations, which is a common computational burden in some of the other personalized federated learning approaches using clustering approaches.

### Weaknesses
The paper's evaluation primarily focuses on graph-based tasks, leaving questions about its generalizability to other types of data and models. While they mention the potential applicability to other domains, this claim remains unverified even in the experimental sense. The method introduces additional complexity through hyperbolic geometry and requires curvature estimation, which could make implementation and tuning more challenging in practice. The computational overhead of working in Lorentz space compared to Euclidean space is not thoroughly discussed, and the paper doesn't address potential numerical stability issues that often arise when working with hyperbolic spaces. Additionally, while the method shows improvements over baselines, some of the gains are modest, particularly in the graph classification tasks, suggesting that the added complexity might not always justify the performance benefits.
The main concerns of the paper are as follows:
 - The paper presents its parameter decoupling strategy as a novel contribution without comparing it with similar approaches in existing literature. The absence of comparisons with previous decoupling methods, particularly [A], makes it difficult to assess the true novelty and advantages of their approach.
- The paper lacks clarity in explaining crucial algorithmic details, particularly regarding curvature estimation. While curvature is central to the method's performance, the paper doesn't adequately explain how it's estimated, updated, or integrated into the training process. The absence of analysis on the impact of different curvature values and their stability leaves important implementation questions unanswered.
- The evaluation is heavily focused on graph-based tasks, with no experimental validation on other common federated learning applications like computer vision or natural language processing (such as FEMNIST). This narrow focus raises questions about the method's applicability and effectiveness in broader contexts, especially given the additional complexity introduced by hyperbolic geometry.
- The paper lacks a thorough analysis of computational overhead compared to Euclidean-based methods. There's no discussion of memory requirements for storing different Lorentz spaces or how the method scales with an increasing number of clients. The communication costs and practical implications in real-world deployments remain unexplored.

### Questions
In addition to the questions and concerns above, I have some other questions:

- Could you elaborate on how the curvature parameters are practically updated during the federated learning process? Specifically, what happens if the estimated curvature is unstable or changes significantly between rounds, and how do you ensure this doesn't negatively impact the model's convergence?
- Could you discuss any potential challenges or modifications needed when applying your method to these domains, particularly regarding the relationship between data heterogeneity and geometric properties in these different contexts?
- Could you provide insights into the scalability of your approach as the number of clients increases, especially considering the additional overhead of maintaining different Lorentz spaces? For instance, provide some results with training times and memory utilization.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a personalized FL method called Flatland. Flatland follows a standard Federated Averaging framework. Each client $c$ first embeds their data into a Lorentz space with a personalized (learned) curvature coefficient $K_c$. They then run local training of a Lorentz model (neural network consisting of so called Lorentz layers that are designed so that if the inputs are in a Lorentz space then so are the outputs). The parameters of this network that correspond to the first dimension of the embedded data are personalized, per client, parameters, while the remaining parameters are shared. The shared parameters are updated using FedAvg, the personalized parameters are kept on the client. 

The paper shows that the specific decomposition proposed still maintained the Lorentz property of the network. The paper then carries out an empirical evaluation of the method on several different graph datasets, for both node and graph classification tasks. It compares to a range of baselines.

### Strengths
* The proposed method is easy to integrate into standard FL training pipelines. It trains using federated averaging and aggregates client updates, meaning it is compatible with privacy preserving techniques such as secure aggregation and differential privacy.

* The originality of the paper is that it is the first to propose using a different Lorentz embedding for each client in order to better capture the differing client data distributions.

* The experiments demonstrate good performance on node classification in real world datasets with small numbers of clients

* The authors provide ablation studies examining the impact of different components of the method

### Weaknesses
I do not believe the paper makes a significant enough contribution, either theoretically or empirically:

Regarding theory, there is a lack of any substantial theoretical contributions

* As far as I can tell Proposition 1 and Corollary 1 are both instant consequences of the definition of a Lorentz network (eq 2), giving a name to the first row and column of the matrix does not require reproving anything. Even more confusing is Corollary 1 and it’s proof, Proposition 1 states that $\forall M, LT(x;M) \in \mathcal{L}$ then of course it is also true that $LT(x;\Phi(M, N)) \in \mathcal{L}$ because it holds for all matrices in the second entry, this does not require a proof as given in the appendix. 
* The remainder of section 6 makes some hand wavy and confusing claims and does not prove any concrete properties or statements about the method. 
* There are many potentially interesting directions here the authors could have taken, e.g. what is the convergence rate, how does the lorentz embedding impact convergence and/or performance, what types of distribution heterogeneity are well modeled by the Lorentz space etc.

Regarding empirical contribution. My overall concern here centers around the empirical evaluation being too narrow. Essentially the evaluation is limited to federated cross-silo, graph datasets, which to me makes it a specialized method rather than a general one, as the authors claim.

* The empirical evaluation is only on graph datasets. The authors present the method as a general personalized federated algorithm and claim that the method is applicable to other data modalities; they present no evidence of this. I am also not convinced that this would be the case, state of the art methods that deal with the most common data modalites (text, image, video, tabular) do not make use of Lorentz spaces. 

* The number of clients in each dataset is very low. Therefore, the experiments do not provide evidence that the method works in a cross-device setting. Crucially, the authors do not mention the cohort size they used in federated averaging, and given the low number of clients in their experiments I am assuming that all clients participate in each round of training. I have concerns about if the method would even work without full client participation in each round (if client A has participated before and client B has not, then A will have already updated their personalized parameters often, while B is starting from initialization, this is going to lead to very heterogeneous shared parameter updates)

* I believe the authors need to provide experiments for other data modalities, with larger numbers of clients as well as partial client participation 

There are some minor typos, e.g. I think in section 5.2 $m^{(l)}$ should be in $\mathbb{R}^m$, not $\mathbb{R}^{m+1}$ and $M^{(l)}$ should be in $\mathbb{R}^{m\times n}$. Also references to tables in section 7 are off and need to be checked e.g. on line 452, Table 3 should be Table 1.

Overall, I would need to see substantial improvements to the theoretical and/or empirical contributions, as suggested in the final bullet points of each section above.

### Questions
* Why do the $v$ parameters not appear anywhere in Equation (4)?
* How does Lorentz space actually model heterogeneity? The paper seems to claim that $x_t$ captures the heterogeneity between client distributions, while the client distributions in Flatland i.e. $x_S$ should be the same. This is an interesting idea but no evidence is provided. I would like to see either theoretical or empirical evidence of this fact.
* Why do you decouple the parameters the way you do? This is related to the above point. It seems that the parameters are decoupled this way so that the heterogeneous feature $x_t$ is fed into the personalized portion of the network $m$ in Equation (4), while the homogeneous features $x_S$ are fed into the shared portion of the network, $M$ in Equation (4). However, as far as I can tell this only works for the first layer since the output of layer 1 $m x_t + M^{(1)} x_S$ will be fed into the shared part of layer 2 $M^{(2)}$ meaning that the updates to shared parameters from layer 2 onwards are still impacted by heterogeneous parts of the client data.
* Does the method work for larger numbers of clients, without full client participation each round?
* What do you mean by statistically significant for the results in Table 1? How can you say that FlatLand outperforms GCFL in graph classification when the mean accuracies are very close with very large overlap of the standard deviation intervals. This looks to me like noise rather than signal.
* It is not clearly defined what the embedding dimension is in Section 7.3. Is this the hidden dimension of the model?

### Soundness
2

### Presentation
2

### Contribution
1
