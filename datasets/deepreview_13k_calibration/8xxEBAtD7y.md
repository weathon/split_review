# Unifying and Verifying Mechanistic Interpretations: A Case Study with Group Operations

- Decision: Accept
- Avg Score: 7.33
- Scores: 6, 8, 8

## Abstract
A recent line of work in mechanistic interpretability has focused on reverse-engineering the computation performed by neural networks trained on the binary operation of finite groups.
We investigate the internals of one-hidden-layer neural networks trained on this task, revealing previously unidentified structure
and producing a more complete description of such models that unifies the explanations of previous works~\citep{chughtai2023,stander2024}.
Notably, these models approximate \textit{equivariance} in each input argument.
We verify that our explanation applies to a large fraction of networks trained on this task by translating it into a \textit{compact proof of model performance}, a quantitative evaluation of model understanding. In particular, our explanation yields a guarantee of model accuracy that runs in 30\% the time of brute force and gives a $\geq$95\% accuracy bound for 45\% of the models we trained. We were unable to obtain nontrivial non-vacuous accuracy bounds using only explanations from previous works.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper contributes to a recent line of work aiming to mechanistically understand the computations performed by neural networks trained on the symmetric group. It takes a step towards this goal by developing an interpretation of the model's computation that can be formally translated into a compact proof of model performance. This compact proof of performance can be measured against the actual performance of the network, serving as a quantitative measure of the quality of a proposed interpretation. The interpretation proposed by the authors is based on their notion of rho-sets, which corresponds to an interpretation of the network learning to become approximately equivariant in each of its inputs. The rho-set interpretation gives rise to a compact proof that can account for the behaviour of approximately half of the models they train. Previous work on the symmetric group came to differing conclusions based on "irrep sparsity" and cosets, but for the approximately 50% of models the rho-set interpretation can account for, it is able to unify the differing interpretations of previous works and show that they are not at odds in these cases. For the other half of models which they are unable to account for with their interpretation, the compact proofs fail to attain non-vacuous bounds. Thus, the authors argue that compact proofs are a concrete way to measure the validity of one's interpretation of neural network computations.

### Strengths
1. Compact proofs are a new way of supporting model interpretations and it seems like they could be interesting, since as the paper states, valid compact proofs can be generated from interpretations one is certain of.
2. For the half of the models that the rho-set interpretation works for, explaining how to reconcile the irrep sparsity and cosets interpretation is helpful.

### Weaknesses
1. While compact proofs are an interesting way to approach interpretability, it's unclear whether they could be used to help interpret neural network solutions for datasets where no or limited explicit information is known about the distribution it was sampled from (e.g. any language task, CIFAR-10, etc.).
2. The fact that the compact proofs derived in this work only get approximately a 50% success rate is concerning, as it implies that the framework using rho-sets is possibly not general enough. The fact that the compact proofs fail to attain non-vacuous bounds for half of the models suggests that the interpretation is incomplete or that there are other relevant factors not accounted for by the rho-set interpretation.
3. Unifying is too strong a word to use in the title when rho-set compact proofs only work approximately 50% of the time. The interpretation's limited scope undermines the claim of a broad unification of prior work.
4. As someone who has familiarity with representation theory, it's still quite hard to understand the rho-set construction and specifically how it can be identified within the network. I must believe that it works since you can write a compact proof (verifier) that empirically matches the network's performance around half the time. However, since it's unclear how you arrived at this rho-set interpretation by mechanistically inspecting the network, it's not clear how other people can use this to come up with compact proofs for other datasets. If compact proofs are to be useful in the field of interpretability, you should be more clear about how you went about figuring this out. E.g. what are the concrete steps you thought of and experiments you ran to define everything in section 5.1 as well as the observations in Appendix B. Being explicit about these things could greatly help the community understand how to integrate and improve interpretations and contribute to compact proofs.

### Questions
1. Can compact proofs be used on datasets without "closed-form" solutions?
2. The way that V_coset is being computed could be fully responsible for the results that cosets have loose vacuous bounds. Reverse engineering the problem qualitatively shows cosets (Stander et al.). I'm wondering if you tried other ways of modeling V_coset? If so, how many other ways did  you try?
3. In section 3.2 why do you take the number of neurons to be equal to the embedding dimension (m)? Is this by chance or necessary for your proofs and interpretation?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
- The paper presents an algorithm by which a one hidden layer MLP network (with embeddings) does composition in $S_5$
    - The algorithm is somewhat involved, but the key step is constructing an expression for $f(z | x,y)$ (eqn 4) that is purely a function of $x^{-1}zy^{-1}$ and maximised at $e$. 
    - This is constructed in an interpretable way using $\rho$-sets, an introduced concept of a set of vectors permuted by irreps of the group G. For a set of $k$ vectors, it needs $k^2$ neurons (one corresponding to each pair of $\rho$-set vectors). 
    - The full network consists of several such constructions, in parallel, using disjoint sets of neurons and possibly different irreps and $\rho$-sets
- This is the same setting as studied by previous mechanistic interpretability works Chughtai et al & Stander et al, but presents a much more detailed algorithm, with a clear story for each parameter and the role of each neuron. 
    - The story provided here helps unify and clarify observations in each paper such as coset concentration and irrep sparsity. 
    - Some aspects of prior work are criticised, such as the specific causal interventions used as evidence in Stander et al
- This explanation is used to provide a lower bound on the model's accuracy, by analysing the margin (correct logit - max incorrect logit) in the idealised model, and comparing that to the worst case logit deviation in the real model.
    - This accuracy bound is proven via a scheme that takes asymptotically less time than brute force trying every input (about 3x faster in practice). This proof fails on some networks, but this seems to correspond to ones where the explanation is imperfect.
    - This is referred to as a compact (i.e. short) proof, inspired by Gross et al
    - The existence of a compact proof seems to be taken as evidence that the explanation is correct, as it gives a faster yet provably valid verification method

### Strengths
1. The authors have found an elegant yet highly non-obvious algorithm for group composition in a single ReLU layer, that multiple prior papers missed. This is a valuable contribution to the literature.
    - Further, the provided explanation clarifies and adds useful context to observations made in prior work
2. The presented compact proofs are highly detailed and rigorous, and actually explicitly go through every key detail, rather than hand-waving annoying points.
3. It demonstrates compact proofs as an interpretability metric in a much more complex setting than prior work (Gross et al)
4. The authors do a good job of highlighting weaknesses, e.g. the times the proof does not work, the failed V_coset proof, and clearly reporting the actual runtimes of the proofs
5. Though highly technical and complex, to the best of my ability to tell, the maths largely checks out. I did not follow the fine detail of all of the appendices.

### Weaknesses
1. This is only studied on $S_5$
2. The compact proof is only 3x faster than brute force
3. The paper is highly technical and at times quite difficult to follow, especially as it builds deeply on 3 prior papers! Though the authors have clearly made an effort to be clear, and this is an inherently complex work. This took me significantly longer than other reviews.
4. The link between finding a compact proof of a bound on accuracy, and verifying a mechanistic explanation, seems somewhat unclear

### Questions
# Major Comments
*The following are things that, if adequately addressed, would increase my score*
1. The key thing that would improve this paper, in my opinion, is making it clearer, especially key technical details.
    - I found sections 4 and 5 difficult to follow - the concepts of coset concentration and irrep sparsity are introduced, without much motivation, and are then not necessary to explain the algorithm. I would personally reverse the flow of 4 & 5.1 and work backwards:
        1. Begin with Eqn 4, and observe that this is bi-equivariant, and sometimes maximised at e (citing lemma F.3)
        2. Show that this is equivalent to Eqn 3
        3. Observe that each term in the sum can be a neuron, and what the relevant w_r, w_l, and w_u need to be for that - we've now constructed a valid algorithm!
        4. Irrep sparsity and coset concentration can then be explained as prior observations, and shown to follow from this algorithm. 
    - I find the term "compact proof" quite cryptic, and it took me until about page 7 to figure out what was going on. A decent part of the confusion is that you use proof to refer to what I'd normally call a program. I would have benefitted a lot from an intuitive explanation in the intro or start of section 6 (ideally both, plus something in the abstract). Something like:
        - A guarantee of model accuracy is a program that can be run to guarantee that models will always give the correct answer at least X% of the time, for some X (i.e. lower bound its accuracy). This can always be done for the brute force "try every possible input" program, but it seems that mechanistic understanding of a model should enable more efficient programs. These are referred to as compact proofs. The efficiency of the program, and closeness of the accuracy bound to the true accuracy, can be taken as metrics of the quality of our explanation.
2. I'm somewhat skeptical of compact proofs as an interpretability metric, for several reasons - I would love to be convinced otherwise though:
    - They bound accuracy, not loss. But a model's performance can be over-determined, with several parallel components each being sufficient to ensure perfect accuracy but all needed to recover the loss, as is common in toy systems like this (you do need to be able to bound the effect of other components, but not necessarily to understand them). IMO an explanation that doesn't understand all such components is incomplete, but it may get fantastic accuracy.
    - It's not clear to me that a mechanistic explanation, even if extremely accurate, should always enable faster proofs. Or even be robust to worst case guarantees at all.
        - While it did in this work, this was *extremely* specific to the setting and explanation, and I don't feel confident there would be other approaches for less mathematically elegant algorithms.
    - The framing in the paper was that being asymptotically faster than brute force was the key thing. But in practice, the coefficient on the compact proof was much worse, and it was 3x faster not 120x faster. IMO 3x is the relevant number here.
    - That said, I find the fact that they seem to identify networks where your explanation is incomplete to be quite compelling.
3. Similarly, I would be excited to see other evidence that your explanation is correct - it makes a lot of predictions about the form of the parameters and activations!
    - Can you learn a and a $\rho$-set that explains a cluster of neurons? Does it have size $k^2$ exactly?
    - How well does your prediction for a neuron's activations match it in practice? What's the MSE and correlation? If you replace the neuron with the prediction (either one at a time, or on the full group for one $\rho$-set) what happens to model performance.
    - How close are the model's parameters (or at least, $w^i_l$ etc) to the predicted form? What if you substitute part of those?
    - I found the claim in Lines 502-503 that causal interventions can only yield weaker positive evidence to be overstated - this applies to the interventions used in Stander et al, but IMO those are pretty weak interventions and not that compelling by the standards of current mechanistic interpretability. This doesn't mean there don't exist more compelling causal interventions.
4. Separately, I'm extremely skeptical that compact proofs will scale beyond very toy networks (let alone to frontier systems). Being robust to worst case scenarios on the entire space of inputs seems highly unrealistic to me for eg a language model or image model. Methods don't have to scale to be interesting, of course, but this limits my excitement about the method. I'd value arguments for why the method might extend to eg imperfect coverage of the input space.
5. I'd be very curious to see how well "the square of the size of the smallest $\rho$-set$" correlates with the probability that $\rho$ is learned, eg using the numbers in Chughtai et al. This would significantly clarify the results in Chughtai et al re universality if true.

# Minor Comments
*The following are unlikely to change my score, but are comments and suggestions that I hope will improve the paper, and I leave it up to the authors whether to implement them. No need to reply to all of them in the rebuttal*
1. Line 243: Explicitly note that we can set w^i_l(x) to whatever we want, it's a lookup table. It's a construction, not a conclusion. This confused me at first
2. I find the term "compact proof" somewhat confusing. To me, proof connotes showing something rigorously about abstract mathematical objects . But perhaps this is just taste, and this notion of proof is common in e.g. the field of formal verification?
3. I don't understand what Figure 1 is trying to show, a shame as you clearly put in effort there! How is S3 mapped to points on a hexagon? What are the terms in the top row with 4 vertices circled? What does adding them mean? What is X_12? Etc I recommend significantly clarifying or changing the figure
4. Obviously, it would be great to replicate the paper's results on other groups! A5, A6, S4 seem natural to try. I predict the results to hold up though.
5. I find the definition of compact proofs somewhat odd - what exactly does it mean to be a valid lower bound for *any* explanation string? It strikes me as odd that your compact proof must first begin by eg verifying if a subset of G is a subgroup, when that seems independent of the model.
6. I personally find Eqns 2 and 3 clearer by replacing $b^T \rho(x)a$ with $a^T \rho(x^{-1}) b$ (which is equal since the transpose of a scalar is the identity), as this motivates the subtraction and substitution more clearly.
7. I liked the point in the appendix that $ReLU(x) = (x + |x|)/2$, though it was not clear to me why the $x$ part cancelled out.
8. Line 109: Causal Scrubbing was introduced in [Chan et al](https://www.alignmentforum.org/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing), not Geiger et al
9. Line 116: It would be good to define the word equivariance here
10. Line 194: I found the claims about embeddings being constant on a coset for a neuron very confusing. It felt like it was asserting this about *all* networks, not explaining a property of a specific constructed network
11. Line 196: What does it mean for a subset of G to be common to a family of cosets? Cosets are subsets of G, so surely the intersection of a family of cosets is a set of subsets, not a subset?
12. Line 436: Why do you refer to neurons as functions $G\to \mathbb{R}$ rather than $G^2\to\mathbb{R}$? They have two inputs, $x$ and $y$, right?
13. Lemma F.3: Are you arguing that all $\rho$ have the decomposition described here? If not, which ones do, and does this correspond to the irreps learned by the model?
14. In table 2 in Appendix G, why does the minimal $\rho$-set size go above 5? Naively, it feels like an irrep of S5 should always be able to permute a set of 5 vectors.
15. Line 452: The claim that the frequency $\rho$ is learned correlates with its minimal $\rho$-set size seems questionable to me. The less frequent 4D one and more frequent 5D one are learned about the same amount of the time in Chughtai et al (Figure 7), despite having $\rho$-set size 10 and 6 respectively, and both less than half as often as the more frequent 4D one (minimal size 5). Your finding may help explain which of the representations at a given dimension is chosen, but it's clearly incomplete

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper unifies two previously proposed explanations for a small neural network trained in a controlled setting. Specifically, it studies the internals of a one-layer neural network trained to perform group composition on finite groups $G$. The input to the model is an ordered pair $(x, y)$ with $x, y \in G$, which are embedded as vectors, and the output is the group element. Prior work studied the same setting and proposed different explanations for the model behaviour: Stander et al. (2024) suggested that individual neurons develop a specialised coset behaviour where their left embeddings remain constant on right cosets and their right embeddings remain constant on left cosets, creating specific subsets $X_i$ where neuron activations sum to zero. Chughtai et al. (2023) found that each neuron operates in the linear span of matrix elements of some irreducible representation, implementing the matrix multiplication through ReLU nonlinearities and then maximising a trace computation to predict the group composition. First, for each of these explanations, the authors point out parts of the behaviour that is left unexplained. They then unify these explanations by showing that neurons are not just using irreducible representations randomly, but are organised in specific circuits. They also show exactly how the ReLU computation works through equation 4, which suggests that the function is bi-equivariant and is maximised when $z = x \star y“. Together these findings provide a more complete picture of the models computations. 

To evaluate the quality of their explanation, they convert their understanding into a verifier program that aims to provide a compact proofs of model performance. Specifically, this verifier aims to use mechanistic insights to reduce the description length of the program (i.e. its runtime). They compare brute-force, the coset explanation (Stander et al.), and their own explanation in terms of accuracy bound and runtime over 100 models trained on the same task. They find that brute-force provides exact accuracy bounds but takes the longest to run (2.2 seconds), the coset explanation does not provide any non-vacuous accuracy bounds, and their explanation obtains a bound of 80 - 100 % for half the models and a non-vacuous bound of 0 % for the other half. Upon inspection, they find that the models where their explanation was not able to obtain non-vacuous bounds, the model converged to other solutions.

### Strengths
- The authors successfully reverse-engineer a neural network trained to perform group operations and provide a more complete explanation than prior work. 
- They rigorously evaluate the quality of their explanation, highlighting that it only explains a subset of solutions a model with this architecture might learn in practice. 
- Their evaluation exposes limitations of causal interventions as positive evidence of explanations.

### Weaknesses
Overall, I think this is a solid contribution without significant weaknesses.

### Questions
- You currently cite the survey of Geiger et al. (2024) for causal scrubbing (line 109). However, I believe it was first introduced in Chan et al. (2022; https://www.lesswrong.com/posts/JvZhhzycHu2Yd57RN/causal-scrubbing-a-method-for-rigorously-testing).

### Soundness
4

### Presentation
3

### Contribution
3
