# Solving Nash Equilibrium Scalably via Deep-Learning-Augmented Iterative Algorithms

- Decision: Reject
- Scores: 3, 3, 3, 5

## Abstract
Computing the Nash Equilibrium (NE) is a fundamental yet computationally challenging problem in game theory. Although recent approaches have incorporated deep learning techniques to tackle this intractability, most of them still struggle with scalability when the number of players increases, due to the exponential growth of computational cost. Inspired by the efficiency of classical learning dynamics methods, we propose a deep learning-augmented Nash equilibrium solver, named Deep Iterative Nash Equilibrium Solver (DINES), based on a novel framework that integrates deep learning into iterative algorithms to solve Nash Equilibria more efficiently. Our approach effectively reduces time complexity to a polynomial level and mitigates the curse of dimensionality by leveraging query-based access to utility functions rather than requiring the full utility matrix. Experimental results demonstrate that our approach achieves better or comparable approximation accuracy compared to existing methods, while significantly reducing computational expense. This advantage is highlighted in large-scale sparse games, which is previously intractable for most existing deep-learning-based methods.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a deep-learning based approach that iteratively approximates Nash equilibrium in normal-form games. The proposed approach shares parameters for all players, and optimizes the parameters by backproping on the Nash approximation loss. It achieves comparable performance as existing deep-learning baselines while scaling better to the number of players and the size of action space.

### Strengths
The writing and presentation is very good. The authors clearly motivates the problem and covers necessary background. The proposed framework is also well motivated and clearly explained. I like that the authors provided lots of intuition behind the method, making the presentation very smooth.

### Weaknesses
- The main weakness is that the experiments are not thorough enough. A central claim is that the proposed DINE framework is more computationally efficient. In order to back up that claim, I would expect to see strong empirical evidence. However, the only experiments are relatively small-scale (except for maybe the polymatrix game with larger N) with utilities generated from uniform distribution [-1, 1]. I don’t think those games are representative enough. Sometimes it appears that the baselines are better (e.g. NFG-transformer has better performance in both the score and the number of iterations in tabular games). For polymatrix games, there are no baseline at all, as the authors claim that they are intractable for existing deep-learning methods. However, in (Liu et al, 2024), they reported performance on polymatrix games, and it’s probably a good idea to compare to that. For Table 2, at least for smaller N values, you can report the baseline performance as well.
- By using i.i.d. stochastic initialization, I believe the permutation equivariance is only achieved in distribution, but not exact for a given instance (a specific learned strategy), it’s not guaranteed to have permutation equivariance. In contrast, (Liu et al, 2024) have exact permutation equivariance.

Siqi Liu, Luke Marris, Georgios Piliouras, Ian Gemp, and Nicolas Heess. Nfgtransformer: Equiv-
ariant representation learning for normal-form games. CoRR, abs/2402.08393, 2024. doi: 10.
48550/ARXIV.2402.08393. URL https://doi.org/10.48550/arXiv.2402.08393.

### Questions
- I’m confused about what K or the number of iteration means in this paper. From Algorithm 2, it appears that K refers to the number of steps it takes for a **learned** network to generate a reasonable strategy profile. However, in your experiments (line 437), you are comparing it to traditional methods that require typically 10^5 rounds of iterations. The cited source (Li et al. 2024) is a survey paper, and the relevant sentence is “Learning dynamics: We conduct T = 105 iterations with zero initialization.” It’s unclear which method is associated with that number of iterations, or whether “iteration” means the same thing as in this paper. Also, the baseline NFG-Transformer (Liu et al, 2024) has K=2-8 in their experiment, which is even smaller than the K=~30 in this paper. It seems against the claim that DINES model has superior convergence.
- Training details are not discussed in this paper. Can you report training curves?
- Please explain the metric used in experiments (e.g. what are the numbers in Table 1 and 2?)
- Since you mentioned that assymmetric actions are important to achieve good loss social welfare, can you show experimental evidence for that? I.e. compare the loss for identical and random initialization.
- One of the claimed advantages of the proposed method is “structural explainability”. I don’t quite get how the resulted algorithm can be interpreted as “learning dynamics”. Can you clarify what learning dynamics means in this context, and how do you deduce that from the resulted algorithm?
- Line 320: “Recording the last mixed strategy allows a residual updating of strategies, which is described later”. I couldn’t find the description on this later in the paper. Could you clarify how the strategy is updated in a residual way?

Hanyu Li, Wenhan Huang, Zhijian Duan, David Henry Mguni, Kun Shao, Jun Wang, and Xiaotie
Deng. A survey on algorithms for nash equilibria in finite normal-form games. Comput. Sci.
Rev., 51(C), June 2024. ISSN 1574-0137. doi: 10.1016/j.cosrev.2023.100613. URL https:
//doi.org/10.1016/j.cosrev.2023.100613.

Siqi Liu, Luke Marris, Georgios Piliouras, Ian Gemp, and Nicolas Heess. Nfgtransformer: Equiv-
ariant representation learning for normal-form games. CoRR, abs/2402.08393, 2024. doi: 10.
48550/ARXIV.2402.08393. URL https://doi.org/10.48550/arXiv.2402.08393.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates deep-learning-based Nash equilibrium learning algorithms. It proposes an algorithm called Deep Iterative Nash Equilibrium Solver (DINES) by leveraging query-based access to utility functions rather than requiring the full utility matrix.

### Strengths
This paper proposes a new deep-learning based Nash equilibrium learning algorithm, which outperforms previous algorithms with lower computational overhead.

### Weaknesses
1.  The presentation should be improved.

                  - The authors should include a figure to clearly illustrate the differences between their network architecture and that of previous works. 

                  - More details about the proposed algorithm need to be provided. In the current version, both Algorithm 1 and Algorithm 2 lack critical information, such as how the network parameters are updated.

                  - The authors claim "improved convergence," which I believe is inaccurate. Proving theoretical convergence for deep learning algorithms is notoriously challenging.

                  - The abstract fails to highlight the paper's contributions. In fact, I would suggest a complete rewrite of the abstract to more clearly emphasize the key innovations of this work.

2. Apart from the issue of representation, the convergence of the proposed algorithm also raises concerns. It is unclear whether the proposed algorithm can guarantee convergence to a Nash equilibrium.

 3. The novelty seems limited because the proposed approach seems to only modify the method to access the utility matrix in the original transformer-based algorithm.

4. The significance of this paper seems limited. By leveraging query-based access to utility functions rather than requiring the full utility matrix, it seems that the proposed method only reduces the computational overhead in sparse games.  Succinct games and other sparse games inherently require less space for representation.   

5. Experimental results are not convincing. In experiments, we can see that the revised transformer-based algorithm cannot significantly outperform the original transformer-based algorithm in most tabular games. The time should be shown as well.
In Polymatrix games, I believe the original transformer-based algorithm can still output results for small games. For example, the result for N=3 and T =16 has been shown in tabular games and should be shown in Polynamtrix games. In addition, the game with N=3 and T=16 and the game with N=4 and T=8 should have similar time complexity for the original transformer-based algorithm.

### Questions
see the weakness

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper describes a deep neural network architecture for computing an approximate NE in normal-form and polymatrix games. The architecture is permutation equivariant and works by querying the payoffs under different play distributions at each layer, resulting in much more efficient computation. Results are reported on normal-form and polymatrix games.

### Strengths
The paper describes computing approximate Nash equilibrium in general-sum N-player games which is a known hard problem. Any work that seeks to compute equilibria faster or more efficiently is important and relevant.

Computation is avoided on activations that are of the order of the size of the payoffs of a game. Instead, computation is done on expected payoffs under mixed play, resulting in significantly smaller computational costs.

### Weaknesses
Some properties of the network, such as permutation equivariance, and transformer layers are contributions of prior work (Duan, Marris, Liu), and this paper borderline claims these as contributions.

The discussions around complexity are misleading. I would probably avoid using “polynomial time” (see questions).

I was surprised that DINES was able to match NfgTransformers performance, despite only getting to query expected payoffs. I worry that the authors have made an error in their comparison to Nfg resulting in a factor of 3 discrepancy between the reported results (details provided in questions).

The questions below expand on the weaknesses. I will be willing to increase my score if I have misunderstood any part of the paper, the questions I have are answered, and any additions I have requested are included. I hope my review can be used to strengthen your work.

### Questions
[Training] The exact training procedure is under-explained. L382 says that NashAppr is minimized. I think the confusion has arisen because the paper introduces the algorithm as an iterative procedure, but I think I am meant to interpret it as a DNN for the purposes of training? I have made some guesses that should be made explicit in the writing:
a) the network is trained over a distribution of games from U[-1,+1]
b) at test time it is evaluated on any game from U[-1,+1]
c) the parameters are trained by backpropping through all the layers.
Questions:
Do you use the same network for different sized games? It seems that the parameters are independent for the size of the game.
I would like to see a training curve. How long does this network take to train?

[Architecture] On the emphasis on “iterative” in the algorithm. Sure, I get the inspiration from iterative methods, but I think the writing over-emphasizes the iterative properties. The model is essentially a DNN with multiple layers, with the layers being iterations. I think the emphasis would make more sense if the weights of each layer were shared, which made me wonder if you explored this?

[Complexity] “Query-based access” “Only KNT utility queries are made”. When I think of a query of a payoff, I would think of reading a single element of a payoff tensor. However line 227 shows that (in a normal-form-game) all N*T^N elements need to be read to calculate the expected payoffs at each layer, which corresponds to TN “queries” as defined in the paper. I find this accounting a little misleading. I appreciate that this sentence “Moreover, as long as the game has succinct representation, each query of utility function can be efficiently computed,...” tempers the claims a bit, but I think more care should be taken not to mislead the reader, particularly in the abstract. I do understand that DINES only has to process much smaller inputs than NfgTransformer and NES. What is the complexity with respect to? Is it number of strategies or joint strategies?

[Permutation Equivariance] Note that NES and Nfgtransformer also incorporate permutation equivariance. I came away from the paper thinkin that permutation equivariance was a contribution. I don’t understand how randomly initializing the initial embeddings preserves permutation equivariance?

[Equilibrium Selection] The question of equilibrium selection should be discussed. There are many, possibly isolated, NE for a game. The method described in this paper finds an approximate one, but does not say anything about which one is being found. This is a known hard problem in the field, and I have no expectation for this paper to solve it, but some discussion on this will strengthen the paper. For example, I imagine the initial embedding will influence the equilibrium that is selected? Was this explored?

[Experimental Results] I noticed that the code for NfgTransformer did not run, so reported results from the NfgTransformer paper were used. The dataset that NfgTransformer was evaluated on is different to the one DINES evaluated on. In particular, Nfg uses a particular distribution of payoffs with variance of 1 for each element, while DINES uses U[-1, +1], which has variance 1/3. Napkin math means that we approximately expect the scale of the payoffs used in DINES to be 1/3 of that in Nfg. Which will result in 1/3 of the expected exploitability. Therefore I believe the paper is underreporting the performance of the competitor model by about 1/3. Aside: I think all these types of papers should report expected exploitability under a uniform distribution for the datasets they sample from to avoid these types of comparison errors. Can you add a row that shows this?

Minor:

L11/L18: “Nash Equilibrium” -> “Nash equilibrium”

L18: “to solve Nash equilibria more efficiently … reduced time complexity to a polynomial level…”. Should change to “solve *approximate* Nash equilibria”. Claiming polynomial for solving Nash is an overreach.

L107: For the learning dynamics section, the authors should clarify that learning dynamics converges to equilibria in time average. While the theoretical and deep learning methods provide a last-iterate solution.

L167: “e > 0”. Perhaps the authors meant “e >= 0”?

L172: “Nash approximation”. I have seen the terms “NashConv”, “NashGap”, and “exploitability” used in the literature. Should another one be introduced?

L190: Polymatrix is also a succinct game. And the paper only looks at dense and polymatrix. I think drop the succinct section?

L203: Marris and Lui (cited elsewhere in the paper) also utilize permutation equivariance.

L231: The capital N has been used for “number of players” up to this point. “n” -> “N”

L266: “allow a centralized update of all inner states in this framework…” I don’t understand this sentence.

L287: “suffers” -> “suffer”

L290: “n” -> “N”

L329: Why not sample a distribution from a flat dirichlet?

L333: “a algorithm” -> “an algorithm”

L392: “poly-matrix” -> “polymatrix”

L400: How many samples were used to evaluate the tabular results?

### Soundness
1

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores the application of Deep Learning to learn the NE, and introduces a new neural network architecture.

### Strengths
This paper investigates the use of deep learning to learn NE, a novel and promising direction. The authors claim that their proposed network architecture significantly reduces time complexity.

### Weaknesses
1. The writing quality of the paper is inadequate. To be honest, when I first read the abstract, I couldn't clearly understand what algorithm the authors are proposing. Even after reading the entire paper, I still don’t have a clear idea of what the authors mean by "iterative algorithms" as mentioned in the abstract.

2. The paper seems too short. I do not find any appendices, and the main content appears to be less than 9 pages. Although ICLR allows papers shorter than 9 pages, most submissions typically utilize 9 to 10 pages for the main body. I am concerned that this paper does not meet the expectations for ICLR.

3. Regarding novelty, the "Related Work" and "Methodology" sections are poorly written. Due to this, I am unable to assess whether the network architecture proposed by the authors is innovative.

4. No runtime comparisons are provided, leaving the effectiveness of the proposed architecture uncertain.

### Questions
1. What are the innovations of your work compared to previous works?
2. Could you provide runtime comparisons?

### Soundness
1

### Presentation
1

### Contribution
2
