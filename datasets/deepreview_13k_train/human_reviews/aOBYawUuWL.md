# Reshaping Reservoirs: Hebbian Plasticity for Improved Data Separability

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
This paper introduces Hebbian Architecture Generation (HAG), a method grounded in Hebbian plasticity principles, designed to optimize the structure of Reservoir Computing networks. HAG adapts the synaptic weights in Recurrent Neural Networks by dynamically forming connections between neurons that exhibit high Pearson correlation. Unlike conventional reservoir computing models that rely on static, randomly initialized connectivity matrices, HAG tailors the reservoir architecture to specific tasks by autonomously optimizing network properties such as signal decorrelation and singular value spread. This task-specific adaptability enhances the linear separability of input data, as supported by Cover’s theorem, which posits that increasing the dimensionality of the feature space improves pattern recognition. Experimental results show that HAG outperforms traditional Echo State Networks across various predictive modeling and pattern recognition benchmarks. By aligning with biological principles of structural plasticity, HAG addresses limitations of static reservoir architectures, offering a biologically plausible and highly adaptable alternative for improved performance in dynamic learning environments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents Hebbian Architecture Generation (HAG), a method for dynamically constructing reservoir computing networks. Unlike standard Echo State Networks (ESNs) with static random connectivity, HAG dynamically forms connections between neurons that have high Pearson correlation. Two variants are introduced: mean-HAG and variance-HAG, which adjust weights based on mean activity and standard error respectively. Starting from a blank connectivity matrix, the method builds excitatory connections based on Pearson correlations. Testing on classification and prediction tasks shows improvements over ESNs in classification.

### Strengths
- The use of Pearson correlation to form connections is novel to my knowledge
- The empirical results on the tested datasets seem reasonable

### Weaknesses
 - The method is not explained very clearly. The exact training algorithm would have been clearer with an explicit algorithm listing.
- The empirical evidence seems to indicate the method works ok, but comparisons with NG-RC [1] would have been useful.
- The sections on Cover's theorem adds very little to the overall paper, and could have been explained in a sentence.
- The implications of analysis in Section 5.1 is not clear

### Questions
- Hows the mean and std calculated? Using what data?
- The Intrinsic plasticity mechanism described in section 3.1.1 also sounds like a homeostasis mechanism.
- E-ESN is not explained in the results tables

Minor:
- Pg. 132-139: There's a "First" and "Third" but no "Second".

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a Hebbian-inspired algorithm for adaptive reservoir computing networks. The algorithm adjusts synaptic weights in the reservoir network as a function of the correlation between neuron pairs, and their corresponding target activity. The paper reports results that outperform traditional and excitatory-only Echo State Networks.

### Strengths
**An interesting Bio-Plausible Approach: Homeostatic Plasticity for Reservoirs**

The main strength of this work lies in its use of homeostasis—a phenomenon prevalent in neural circuits—to improve reservoir learning. The results presented are both promising and impressive, especially given the simplicity of the homeostatic constraint (i.e., maintaining Δz between -1 and 1). I also appreciate the paper’s thorough evaluation across both classification and regression benchmarks.

### Weaknesses
 **Concerns with Methodology**

- The calculation of Pearson correlation between neuron pairs is unclear. Specifically, it's not clear if the correlation is calculated over the entire time series or a sliding window, and how this choice impacts the dynamics of the reservoir. Furthermore, the text does not specify if the correlation is computed using the raw neural activations or some transformed version of it, which could significantly alter the results.
- The choice of correlation bounds \(-1\) and \(1\) seems arbitrary—can you explain the reasoning behind this? It is unclear why these specific bounds are chosen, and how the algorithm would behave with different bounds. The lack of justification for these bounds raises concerns about the robustness and generalizability of the approach.
- What threshold is used to determine "highly correlated neuron pairs" for establishing new connections? The manuscript does not specify how the algorithm selects which of the most correlated pairs will form a new connection. Is it a fixed number, a percentage, or a dynamic threshold? This lack of clarity makes it difficult to reproduce the results.
- The statement, "Weight needs to be decreased by \(\delta_w\)," lacks detail—how is \(\delta_w\) calculated? The manuscript does not provide a clear explanation of how the weight adjustment parameter \(\delta_w\) is determined. Is it a fixed value, a function of the correlation, or some other parameter? Without this information, it's impossible to understand the dynamics of weight modification.
- Why are connections pruned at random? Random pruning seems like an arbitrary choice, and the manuscript does not justify why a more structured approach isn't used. It is unclear why the authors don't consider pruning connections based on their contribution to the network's performance or some other metric.
- Figure 2 appears arbitrary; it is neither referenced in the text nor adequately explained in its caption. The figure's purpose and relevance to the presented methodology are unclear, and it does not seem to contribute to the understanding of the algorithm.
- The section on Cover's theorem seems irrelevant and unnecessary, as the theorem is not mentioned again after this section. The inclusion of Cover's theorem does not seem to have a direct connection to the rest of the manuscript, and it is unclear why it is included.
- How is the target activity \(\rho\) determined? The manuscript does not provide a clear explanation of how the target activity \(\rho\) is determined. Is it a fixed value, a function of the network's activity, or some other parameter? Without this information, it's impossible to understand the dynamics of the homeostatic mechanism.

### Questions
Could the authors clarify the concept of 'Suitability Characterization'? This is mentioned as a key contribution of HAG.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors present Hebbian Architecture Generation (HAG), an innovative method that dynamically adjusts synaptic weights within RNN to enhance the quality of their representations. Experimental results demonstrate that HAG achieves superior performance compared to traditional Echo State Networks across a range of predictive modeling and pattern recognition benchmarks.

### Strengths
***1.*** The authors propose a new approach to Echo State Networks called HAG.

***2.*** HAG achieves improved performance compared to the original ESN method.

***3.*** The authors assessed the correlation among neural states using Pearson correlation.

### Weaknesses
 ***1.*** The motivation for the method in the article is unclear; in other words, it is not evident why HAG was proposed, and the article does not provide a clear explanation. Additionally, it does not specify the main problem that the article aims to focus or address. The paper lacks a discussion of the limitations of existing ESN methods that HAG is designed to overcome. It is unclear what specific representational deficiencies in standard ESNs this method is intended to resolve, and how the proposed Hebbian learning rule directly addresses these deficiencies. Without this context, the novelty and necessity of HAG are difficult to assess.

***2.*** There is no comparison with other methods in the results, only a comparison with the original ESN. This means that the method merely offers an improvement but does not demonstrate how effective it truly is. Additionally, there are no meaningful characteristics, aside from higher accuracy, to differentiate it from other methods. The absence of comparisons with other state-of-the-art methods in reservoir computing or similar recurrent neural network architectures makes it difficult to gauge the true impact and competitive advantage of HAG. The paper needs to demonstrate not just an improvement over the baseline ESN, but also how HAG performs relative to established alternatives. The lack of analysis on computational cost, parameter sensitivity, or convergence properties further limits the understanding of HAG's practical utility.

***3.*** The descriptions of the figures are unclear, making it difficult to understand the significance of the data presented. The figures lack detailed captions explaining the specific variables being plotted, the axes' units, and the implications of the observed trends. For example, the meaning of the different curves in Figure 2 and the significance of the subplots in Figures 3 and 4 are not readily apparent, hindering the reader's ability to interpret the results and validate the claims made in the paper.

### Questions
***1.*** The authors need to explain the motivation behind proposing this method, why it was developed, and its significance.

***2.*** The authors should expand their experiments to demonstrate the true effectiveness of their method, as the current experiments only serve as a basic validation. This includes providing more detailed results, explanations of Pearson correlation, and other relevant metrics to substantiate the method's impact.

***3.*** The purpose of Figures 3 and 4 is unclear; a more detailed explanation is needed to clarify the meaning of each subplot.

***4.*** Figure 2 does not provide any more useful information, the different curves are mixed together, and the problem illustrated by this figure is not clear.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper suggests a method for self-organizing reservoirs that obey a mixture of a hebbian rule as well as a mechanism to grow connections, which is a function of pearson correlations between neurons outside of homeostatis; and pruning, which is random. The objective of these adaptive mechanisms is to de-correlate features within a reservoir in order to allow for better (linearly seperable) projections. The architecture that is used is an RNN of approximately 500 nodes (depending on the task). Across a variety of tasks, including several audio classification tasks and complex-system time-series prediction tasks, the authors showed that their methods (Hebbian Architecture Generation) HAG achieved consistently better performance when compared to standard echo state networks.

### Strengths
Originality: While many of the components of the methods used in this paper have been used elsewhere, I believe it is original to combine them with reservoir computers, and in this sense, this is an original implementation of some known methods.

Quality: The authors did well to select a broad set of tasks, and especially some difficult tasks, taking care to ensure performance scores and training were done with care by implementing appropriate cross-validation techniques.

Clarity: The goals and intentions of this project are sound and well motivated. Reservoirs are, by their nature, extremely sensitive to their initializations, and there are a number of papers that discuss clever ways to initialize these models in order to have them behave reasonably well across different tasks. It is likely that no single initialization technique would work for all tasks, and so it makes sense that an adaptive method, inspired by neural plasticity would be a step in the right direction.

Significance: I believe the project has the potential to be signficant as methods for self-organized/adaptive unsupervised networks are still not well understood and by and large do not have the same performances as more standard machine learning practices. Discovering new and efficient methods to modify architectures online, I believe, will be important in understanding and implementing biologically inspired learning algorithms in the future. This project's implementation explores a reasonable mechanism for architecture modifications online. However, this signifiance is slightly overshadowed by some lack of detail, which I try to outline below.

### Weaknesses
To my understanding, the novel contribution of this paper is largely contained in the growth/pruning mechanism introduced. The hebbian rule itself looks to me to be relatively standard (though some details are still unclear to me, for example in deciding exactly *which* connection is strengthened when $\Delta z < -1$), so the biggest difference is in using Pearson correlations to decide when new connections form. However, there is not much information in the rest of the paper of the dynamics of this rule over time. What effect does this have on the architecture? Are there clusters in the end? What kind of connectivity does it result in? What is the difference between the spectral radius before and after the mechanism? If this is the novel contribution of the paper, I would have expected quite a bit more detail on the effect this mechanism has on the architecture, but the only result that is shown is in figure 5 and 6 and I'm not sure if figure 6 is telling the story the paper claims it does (see below on more comments on figure 6).

edit: Looking further into it, I realize that actually the plasticity rule that is being used is not hebbian at all, it's actually a homeostatic rule. If I'm not mistaken, a hebbian rule involves some type of product of activations, whereas the rule here is just trying to match a target rate for each individual neuron? Is it not incorrect then to call this a hebbian rule?

Furthermore, the usage of pearson correlations for all neurons very explicitly makes this rule global both in space (nodes) and time, as computing the correlation values requires a large enough timeseries. So I have some problems with how this rule is being pitched/described. It's neither exactly hebbian nor local. I think it ought to be described more accurately and acknowledging these global elements.

# Some general comments:
- The paper would benefit greatly from an appendix which delves more into the detail of the methodology used and visualized some of the dynamics of the self-organizing principles. 
    - how does the pruning/growing mechanism affect the architecture of the network over time? How significant are the differences to the random networks? To a network with the hebbian rule without the pruning/growing? At the moment I have no idea how much this mechanism, which I have to say is really the only novel part of the model as far as I understand, is actually benefiting the reservoir. Your performance scores are alright, but some of them are hardly different from the ESN. You have one score that is significantly better for the SPEECHCOMMANDS tasks. Is it possible that the growth/pruning is doing more there? Can you quantify how much this is doing?
    - an ablation analysis, if you remove the growth/pruning, do your results diminish? Is it important? 
    - after your hyper-parameter search, what values were successful? Is there a heat-map that you can make for the hyperparameters to show what worked and what didn't? If I were to try to recreate your results I would have no idea what results you had to even compare to!
- the figures in the paper are on the very edge of legible and need their sizes and fontsizes standerdized. Please look up the page widths of the paper and make sure your figures have the right sizes and dpi settings. (In matplotlib you would set the figsize=( ) parameter.)
    - Also, the linewidths, axis labels and legends need some work. For example figure 3, the left and right-most panels have their y-axis as "Value". That is not an informative label.
    - Same for figure 2 and 4.
    - Figure 2, though somewhat useful to see (in the appendix) is taking up space that I would rather be used to explain the growth/pruning mechanism.
    - Figure 2 also has some weird text at the 0 mark which is illegible. The legend is also hardly noticably different between the different shades. But I think you should remove this figure anyway or put in appendix.

# Typos and unclear things
- the values $\Delta w$ and $\delta w$ (why are they different?) are not clear to me (is it the "weight increment" in the table? Actually, all variables in the table that have already been introduced in the paper should probably include their symbols.)
- line 165 typo: "we then identifying highly correlated neuron pairs we establishes a connction" needs rewriting
- line 166 typo: "if $\Delta z_i > +1$ connections weight" should probably read "if $\Delta z_i > +1$ the connection weight needs to be..."
- line 172: "maximum number of synaptic partners, $\gamma$" isn't this just the degree of the node? It would probably be more clear if it was written that way
- line 174 typo: "which might limits the..." should be "which might limit the"
- line 297 typo: "actual targetst" 
- there were a few more small typos so I won't list them all, but the paper need some editing still

# References (edit 30/10/2024)
There are a number of extremely relevant references and works that I think this project doesn't cite that it should.
- [Homeostatic Plasticity and External Input Shape Neural Network Dynamics](https://journals.aps.org/prx/abstract/10.1103/PhysRevX.8.031018)
    - As this is largely a homeostatic rule and not a hebbian one, I was surprised to not find this work in the citations.
- [SORN: a self-organizing recurrent neural network](https://www.frontiersin.org/journals/computational-neuroscience/articles/10.3389/neuro.10.023.2009/full)
    - similarly, another project with very similar goals is described here, and although they use inhibitory neurons as well, it is too relevant not to acknowledge.


Overall: I would say this paper could use another iteration of development. It is currently lacking the detail for someone to recreate the work, firstly. And secondly, considering that it is utilizing techniques that have been used before and are relatively simple (this is a good thing), and that it is doing so in a relatively small increment (again, this is not bad), this requires that this increment be well justified and argued for. At the moment, it is not at all clear to me how the components of this metholodgy contribute to the final result. We only see the final result as a table of performances, but it is not clear to me in what way the adaptive mechanisms contributed to this. This needs to be made clear, and the mechanisms need to be understood in their role for changing the architecture and clustering correlated features.

### Questions
I made a list of questions in the Weaknesses section (regarding stuff I would have liked to see in the appendix for example that I think are required for me to know for sure that the methods introduced in this paper are actually responsible for the results presented, as well as for reproducability reasons). 

Some more questions I have that are less crucial but have piqued my curiousity are:
- How does performance scale with model size? Some of the results compared with the ESNs are not too different, and some are quite a bit better. If you scale the model to smaller or larger networks, are these differences conserved? Does your model adapt better or worse when the size changes?
- I think you compared your results to standard ESNs, and according to your table, there were a range of spectral radii that were used to initialize random networks. Which spectral radii did you use when making your performance tables? There is some literature on "best practices" for initializing reservoirs that specifically detail the sensitivity/performance of reservoirs on these settings. Did you use these "best practices" or were the ESNs handicapped by having random initializations? This part is not clear to me and unfortunately this is what needs to be made completely uncertain for the results of your method to be interesting.
- In figure 6, the evolution of the moving cumulative explained variance in panel (a) starts quite high, at around 22-25 and then decreases a bit down to ~19. Why does it start so high? In panel (b) the random reservoir starts around 2. If during training is when the growth/pruning happen, shouldn't panel (a) also start very low and then increase to higher principle components? If the growth/pruning is already done before making this figure, what was the point of this figure? I would be curious to know how the INITIAL network behaves and then how the growth/pruning + hebbian learning complexifies the dynamics. Right now it's not clear to me why figure 6 looks the way it does. 
- line 102: "according to a self-organised local rule" I understand that the hebbian part of this mechanism is looking at individual neuron activity and in that sense it's local, but not much else is local in this model. As I understand it, the network architecture is fully connected (or connectable, so every neuron *could* in principle be connected to any other neuron) and also the growth/pruning mechanism is fully global as well. I would be careful when phrasing the rule as such, because actually there is a mixture of global and local interactions here.

### Soundness
2

### Presentation
3

### Contribution
2
