# Learning-based Mechanism Design: Scalable, Truthful, and Continuum Approaches for Utility Maximization

- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 3, 3, 3

## Abstract
Mechanism design is a crucial topic at the intersection of computer science and economics. 
This paper addresses the automated mechanism design problem by leveraging machine learning and neural networks. 
The objective is to design a **truthful**, **expressive** and **efficient** mechanism that maximizes the platform's expected utility, given that the players' types are drawn from a pre-specified distribution.

We present a general mechanism design model that captures two critical features: hidden information and strategic behavior. 
Subsequently, we propose the **PFM-Net** framework, which parameterizes the menu mechanism class by function approximation and identifies an optimal mechanism through ingenious optimization techniques. 
We also provide both theoretical and empirical justifications for the advantages of our approach. 
Experimental results demonstrate the effectiveness of PFM-Net over traditional and learning-based baselines, 
enabling the PFM-Net framework to serve as a new paradigm for automated mechanism design.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper uses the MenuNet (Shen et al., 2018) idea to optimize a general quasi-linear objective over multiple players and multiple items. In particular, the feasible allocation set X is the product of the feasible allocation set for each individual player i, which implies that there is no constraint on the total supply of each item (each item could potentially allocate to multiple players).

The results are compared with other mechanisms empirically.

### Strengths
Unless I misunderstood the feasible allocation set, I didn’t see much strength.

### Weaknesses
The problem being solved in this paper is a trivial extension of the MenuNet (Shen et al., 2018) to multiplayer setting with individual-wise allocation constraints. The core idea of MenuNet is to learn a mapping from the reported values to the optimal allocation and payment, which is achieved by training a neural network to mimic the optimal mechanism. The extension to a multi-player setting where each player has their own allocation constraints, while practically relevant, does not introduce significant theoretical or algorithmic novelty. The key challenge of extending MenuNet to general multi-bidder setting is to handle the feasibility constraint properly (i.e., each item can only be allocated to at most one bidder). 

This challenge is referred to as “menu compatibility” and first solved by GemNet (Wang et al, 2024b), who solve the compatibility issue through a combination of a price adjustment and MIP (mixed integer program).

This paper, however, drops the only challenge of generalizing MenuNet to the multi-bidder setting. So I cannot see any real contribution to the literature (unless I misunderstood this part).

### Questions
Please properly mention the key result of MenuNet in your second paragraph, and explicitly compare your approach with theirs.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
There has been a lot of recent research on designing revenue-optimal, strategy-proof auctions through the use of neural networks and machine learning tools. However, existing approaches often fall short of meeting all desired properties: exact truthfulness, expressiveness, and efficiency. For instance, RegretNet does not ensure exact truthfulness, AMA mechanisms lack expressive power, and MenuNet can be computationally inefficient. This paper presents PFM-Net, a framework designed to address all three objectives through a learning-based approach.

The authors propose a full-menu mechanism that uses neural networks to parameterize pricing functions—determining how much agents are charged for specific bundles based on their valuations. This framework incorporates insights from economic theory, such as agent independence, convexity and monotonicity, to achieve incentive compatibility and a no-buy-no-pay rule to satisfy individual rationality. The optimization is an alternating process: first, allocations are optimized for the players given fixed pricing functions; then, the neural network parameters are adjusted to optimize revenue for the auctioneer.

The framework is initially evaluated in a single-bidder, multiple-goods setting. It is adaptable to other objectives, such as social welfare maximization. To demonstrate this flexibility, the authors include an experiment with a social planner setting involving multiple agents and multiple goods.

### Strengths
S1. PFM-Net leverages insights from economic theory, including agent independence, convexity, and monotonicity, to ensure incentive compatibility and no-buy no-pay rule to satisfy individual rationality. These designs seem to be an improvement over architectures presented in RegretNet

S2. Avoidance of Explicit Menu Enumeration  
Traditional menu-based mechanisms often require enumerating all possible menu options, which can be computationally prohibitive, especially as the number of items grows. For instance, even a deterministic mechanism for a single buyer with $m$ items would need $2^m$ menu options, creating scalability challenges. PFM-Net, however, avoids this by not requiring explicit enumeration of the menu. For each auction instance, it optimizes the agent's objective directly based on the pricing functions. This means allocations are determined dynamically by maximizing the agent’s utility under the current pricing function, allowing the model to handle large settings without incurring the overhead of menu enumeration.

### Weaknesses
W1. Missing Baselines  
RochetNet, the current state-of-the-art for single-buyer settings, should be included as a benchmark, as other methods generally reduce to RochetNet in this context, making it a sufficient point of comparison. Additionally, the optimal mechanism for up to six items is given by the SJA mechanism (referenced in the paper as Giannakopoulos and Koutsoupias) [1]. Please include this under OPT for $S_5$. This mechanism can be extended for larger m using a recursive formula, with results available up to m = 10 in the RegretNet paper, where it is also conjectured to be optimal. This makes SJA an essential baseline for evaluating the proposed approach.

Moreover, it would be interesting to test the model’s performance in a setting with a single additive bidder and two items, where the bidder's values are independently drawn from a Beta distribution (α=1, β=2). Prior work [2] has shown that the optimal mechanism in this setup involves an infinitely sized menu, providing a valuable test case. Additionally, including settings where randomization is essential would show how well this approach performs for non-deterministic settings.

W2. Lack of Moderate/Large-Scale Experiments  
The paper currently lacks experiments involving moderate to large-scale settings. RegretNet already performs well with very low regret for the small scale settings shown in the paper. For smaller settings at least, one could consider Regretnet to be potentially exactly truthful. To fully demonstrate PFM-Net's advantages over regretnet, it would be beneficial to include tests with multiple agents and items (e.g., n,m≥2) 

W3. Writing and Clarity  
The writing is generally clear and accessible until Section 4. I found myself frequently switching between the appendix and the main paper to fully understand the methodology. Including the learning algorithm or a pseudo-code in the main paper would improve readability. Additionally, clearly noting in the main text when specific technical details, such as the handling of over-allocations, are explained in the appendix would be helpful as well.

### Questions
This approach shares notable similarities with RegretNet. Rather than having separate networks for allocation and payment, PFM-Net combines these into a single payment network with hardcoded constraints like convexity and monotonicity. The training process is also comparable: the proposed approach alternates between computing the allocation (the analogous step is finding the misreport in regretnet) and optimizing the payment function (updating the weights of RegretNet). Equation 11 is the also the same as RegretNet's objective (with the missing L2 penalty term). 

For larger settings, it’s likely that PFM-Net would encounter similar issues to RegretNet with gradient-based allocation computation. Testing the proposed approach's exact violation (i.e., the term involving ReLU in Equation 11) at test time, preferably with multiple initializations of x, would be informative. For smaller settings, RegretNet incurs very low regret (and recovers optimal solutions wherever known). For larger configurations, further evaluation is needed to verify that PFM-Net’s allocation computation can overcome these scaling challenges that RegretNet faces in computing the misreports.

### Soundness
2

### Presentation
2

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
This paper explores deep learning methods applied to mechanism design, focusing on multi-buyer, multi-item scenarios where $ n $ represents the number of buyers and $ m $ the number of items. The primary focus is on menu mechanisms. For example, in a single-buyer context, a menu mechanism is defined by a set $ X \subseteq [0,1]^m $, where each allocation vector $ \vec{x} \in X $ indicates the probability that the buyer will receive each item. This mechanism is coupled with a pricing function $ p(\vec{x}) $, and the buyer selects the allocation vector that maximizes their utility.

The authors attempt to establish that the class of truthful mechanisms is equivalent to the class of menu mechanisms with convex pricing functions (I found this proof somewhat difficult to follow, as I elaborate in the Weaknesses section.)  Building on this theoretical foundation, the authors design a neural architecture. While the main text does not provide details on the architecture or algorithm, the core idea is to use a convex function to represent the payment function, which is optimized during training.

### Strengths
The paper's experiments suggest that the authors may be onto something promising with their architectural design. The revenue results in Table 1 indicate strong performance relative to baselines like UM-GemNet, showcasing the potential effectiveness of their approach.

### Weaknesses
 - I found the proof of the main theoretical result, Theorem 3.4, challenging to follow. This theorem claims that the class of truthful mechanisms is equivalent to the class of menu mechanisms with convex pricing functions, but several parts of the proof were confusing:
  - On line 1018, it’s unclear what is meant by treating $ x_i^d $ and $ p_i^d $ as free variables $ x_i $ and $ p_i $. First, since these are functions, it’s confusing to call them variables, and second, because they are defined by the input mechanism $ M^d $, it’s even more confusing to refer to them as “free” variables. The notation here is particularly unclear, as it seems to suggest that the functions $x_i^d$ and $p_i^d$ can be arbitrarily replaced by other functions $x_i$ and $p_i$ without any justification. This substitution needs to be rigorously defined, and the implications of such a substitution on the overall proof need to be clarified.
  - On line 1022, I’m unsure what is meant by saying $ \tilde{u}_i(t) $ is constant with respect to $ x_i $ and $ p_i $. By definition, $ \tilde{u}_i(t) $ depends on $ x_i^d $ and $ p_i^d $, so it doesn’t appear to be constant with respect to these terms. The argument that $ \tilde{u}_i(t) $ is constant with respect to $x_i$ and $p_i$ is not well-justified. The dependence of $ \tilde{u}_i(t) $ on $x_i^d$ and $p_i^d$ is explicit, and it is not clear how these terms can be treated as constant. This claim requires a more detailed explanation of the underlying assumptions and the mathematical manipulations involved.
  - In Equation (5), the supremum is taken over $ t_i $, but the line before mentions $ p_i $ should be minimized. The connection between this minimization and the supremum in Equation (5) is unclear. The logic connecting the minimization of $p_i$ and the supremum over $t_i$ in Equation (5) is not clear. It is not obvious why minimizing $p_i$ would lead to the specific form of the supremum in the equation. A more detailed explanation of how this minimization relates to the overall goal of establishing the equivalence between truthful mechanisms and convex pricing functions is needed.
  - The paragraph titled “Prove the first statement” on line 1049 is also difficult to interpret. Since $ \tilde{u}_i(t) $ is a function of $ x_i^d $ and $ p_i^d $, whether $ \tilde{u}_i(t) $ is convex should depend on the properties of $ x_i^d $ and $ p_i^d $ (e.g., whether or not they themselves convexity). The argument that $p^f_i(x_i; t_{-i})$ is convex because it has the form of a Fenchel conjugate is not sufficiently explained. It is not clear why the specific form of Equation (5) implies convexity, and a more detailed explanation of the properties of Fenchel conjugates and their relevance to the proof is needed. The connection between the convexity of $p^f_i$ and the properties of the underlying mechanism also needs to be clarified.
- Section 4 would benefit from more information on the algorithm.
- In terms of experiments, prior work (e.g., UM-GemNet) evaluates performance on a wider range of distributions beyond $ U([0,1]) $. This paper should expand its set of benchmarks to allow for a more comprehensive comparison.
- There are also numerous grammatical issues throughout the paper. I recommend using a tool like Grammarly to identify and correct these. Lastly, it’s advisable to avoid terms like “ingenious” in the abstract when describing one’s own method.

### Questions
Could you please address my confusions regarding the proof of Theorem 3.4?

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
There has been much recent progress in using neural networks for mechanism design. Current successful approaches are either not fully expressive, are restricted to a single agent, can't guarantee strategyproofness, or require costly postprocessing. The authors of this paper present a new method that is fully expressive and works in general settings, and is strategyproof, yet is claimed not to require costly postprocessing. The key idea is rather than searching for allocation/payment rules as functions of types, they work in the dual space and compute a pricing function over each possible allocation of the mechanism. They show that truthfulness is equivalent to a convexity property of this pricing function. There are many good methods for enforcing convexity of neural networks, so the authors use these to train neural networks representing the pricing function on a couple mechanism design problems, and achieve good performance.

### Strengths
The paper tackles a key problem in mechanism design and tries to push things forward in a very creative way. The core idea is clever and original. The authors do have some successful experiments and successfully prove many important mechanism design properties for their method.

### Weaknesses
# Presentation

The biggest weakness of this paper is in its presentation.

There are frequent grammar and usage errors, and it might be good to fix them, but these errors don’t harm comprehension, so this is not so important.

However, the organization and structure of the paper is extremely difficult to follow, far beyond the usual problems of space-limited conference papers. The definitions are unusual and non-standard, many points jump around frequently, the proofs are not well-organized, and I find myself trying to guess at what the authors are doing based on my knowledge of mechanism design, rather than learning it from the paper itself.

Overall the presentation is confusing enough that I have a hard time following the paper, even though I completely understand all background work. There are many good aspects to this work but the poor presentation makes it hard to really tell what’s going on.

# Experiments

One of the main exciting things about automated mechanism design is its use in solving the wide-open problem of revenue-maximizing DSIC auction design. There are many auction design benchmark problems in the papers the authors cite (GemNet, RegretNet, AMA) but the authors choose to compare to none of these benchmarks, instead picking only two problems, one of which is less interesting (single buyer) and one of which is not standard.

If the authors could run their method on some of the same benchmarks as in the RegretNet/GemNet papers, and hopefully produce similar plots visualizing the learned mechanisms, it would significantly increase confidence that their method works well. I think any claimed competitor to GemNet must tackle some of those problems shown in the GemNet paper (e.g. recover the Yao auction, or 2x2 uniform additive buyers, at the very least).

# Full Expressiveness and Supply Constraints

The authors claim their method is fully expressive, which seems to be true as far as I can tell. It is also true of GemNet (their main point of comparison).

The main weakness they point out with GemNet is that it requires a costly post-processing step on a discrete grid. The purpose of this post-processing step is to achieve “menu compatibility” — during learning GemNet may choose menus such that when all bidders choose their favorite menu item, some items are oversold, and the post-processing step adjusts prices to prevent this.

So the key point is the post-processing step is only required for problems where menu compatibility is an issue. But in both of the problems studied in the experiments in this paper, menu compatibility would not be an issue — GemNet also is fully expressive and requires no postprocessing!

Although they don’t deal with it in experiments, in principle their method can deal with supply constraints of the sort that show up in auctions. This is discussed quite briefly in section F.1 (I think it belongs in the main body or at least should be mentioned more prominently as it is very important). However there are unresolved issues to make this work in practice. Perhaps these issues can be overcome more efficiently than the GemNet postprocessing, but the paper gives no evidence one way or the other. (Also, side note — equation 13 seems not to “type check” — a vector proj(x, X) is subtracted from a scalar)

### Questions
Although this review is somewhat harsh, I do want to give the authors encouragement for pursuing a clever and original idea, and I think in the future this could become a great paper.

The authors are welcome to respond to any points in my review they want to, and to correct any errors or misunderstandings of mine. I would be happy to engage in discussion.

### Soundness
2

### Presentation
1

### Contribution
2
