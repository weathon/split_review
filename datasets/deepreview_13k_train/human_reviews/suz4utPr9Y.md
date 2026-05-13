# How efficient is LLM-generated code? A rigorous & high-standard benchmark

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
The emergence of large language models (LLMs) has significantly pushed  the frontiers of program synthesis. Advancement of LLM-based program synthesis calls for a thorough evaluation of LLM-generated code. Most evaluation frameworks focus on the (functional) correctness of generated code; efficiency, as an important measure of code quality, has been %largely 
overlooked %\wz{overlooked}\RZ{revised}
in existing evaluations. In this work, we develop ENAMEL (EfficeNcy AutoMatic EvaLuator), a rigorous and high-standard benchmark for evaluating the capability of LLMs in generating efficient code. Firstly, we propose a new efficiency metric called eff@$k$, which generalizes the pass@$k$ metric from correctness to efficiency and appropriately handles right-censored execution time. Furthermore, we derive an unbiased and variance-reduced estimator of eff@$k$ via Rao--Blackwellization; we also provide a numerically stable implementation for the new estimator. Secondly, to set a high-standard for efficiency evaluation, we employ a human expert to design best algorithms and implementations as our reference solutions of efficiency, many of which are much more efficient than existing canonical solutions in HumanEval and HumanEval+. %This sets a high standard for efficiency evaluation. \wz{add: this provides a high standard for efficiency evaluation.}\RZ{sounds good. added}
Moreover, to ensure a rigorous evaluation, we employ a human expert to curate %write\hh{curate}\RZ{Maybe ``create''? To my understanding, ``curate'' means selecting and organizing existing things}
strong test case generators to filter out wrong code and differentiate suboptimal algorithms. %With our generated strong test cases, we found 11 canonical solutions in HumanEval and 4 in HumanEval+ are wrong, and 34 in HumanEval and 27 in HumanEval+ exceed the time limit during evaluation. 
An extensive study across \NumLLMs{} popular LLMs using our benchmark \Ours{} shows that LLMs still fall short of generating expert-level efficient code. %Benchmarkd with our expert-written reference solutions, even the strongest commercial LLM GPT-4 has low eff@1=0.454 despite its high pass@1=0.831. % 10 models even have eff@1 below 0.1.
Using two subsets of our problem set, we demonstrate that such deficiency is because current LLMs struggle in designing advanced algorithms and are barely aware of implementation optimization.
Our benchmark is publicly available at \OurRepo{}. %\wz{made minor changes for the abstract\RZ{Thanks!}. is the abstract too long? if so, need to condense a bit\RZ{The abstract of the HumanEval+ paper has a similar length. maybe it's ok? our abstract is a bit long because we made many contributions. If we need more space later, we can condense it then}}\hh{i think as long as the 'main body' (=introduction) starts in page 1, we should be fine. if we need more space for that, we can consider make the author info in one row.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a systematic benchmark for efficiency of LLM generated code. The paper presents the eff@k metric, which captures efficiency of generated code (the expected maximum efficiency score of $k$ independent code sample). The presented metric is the first that can capture the relationship between code efficiency and the sample size k. Expert solutions and expert test cases make this benchmark a compelling baseline.

### Strengths
- Very nice and clear presentation 
- A clear and rigorous technical treatment of evaluation timeout (right censoring)
- Human expert solutions as an efficiency target 
- Human expert test cases covering tricky corner cases

### Weaknesses
 - I would appreciate a comparison with previous metrics, even the naive ones, to see whether the empirical effect of this new metric is that models/problems are given a different ranking. 
- Not evaluated with a prompt that asks for an efficient solution, I suspect that a better prompt would make this entire suite too weak for being a competitive benchmark



### Questions
- I understand the theoretical importance of Rao-Blackwellization in this case, but what is the empirical effect? 

- Effibench presented an efficiency-benchmark with 1,000 coding problems, where ach problem is paired with an executable human-written canonical solution, which obtains the SOTA efficiency on the LeetCode solution leaderboard. I would not classify it as a sporadic attempt, what makes you view it as such?

- Does it make sense to also consider space complexity in your benchmarks? For example: 

Your optimized solution for #40: 
```
def has_triplet_sum_zero(l):
	n = len(l)
	if n < 3:
		return False
	for i, x in enumerate(l[: n - 2]):
		buf = set()
		for y in l[i + 1 :]:
			if y in buf:
				return True
		buf.add(-x - y)
	return False
```

Suggested solution: 
```
def has_triplet_sum_zero(l):
    l.sort()  # Sort the list first
    n = len(l)
    
    for i in range(n - 2):
        # Use two pointers to find if there's a pair with sum -l[i]
        left, right = i + 1, n - 1
        target = -l[i]
        
        while left < right:
            current = l[left] + l[right]
            if current == target:
                return True
            elif current < target:
                left += 1
            else:
                right -= 1
    
    return False
```

Uses two pointers, has the same time complexity, and reduces space complexity from $O(n)$ to $O(1)$.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a new benchmark for evaluating the efficiency of code generated by LLMs. The authors select 142 problems out of the 164 problems in HumanEval and HumanEval+ (they excluded trivial problems with Θ(1) time complexity). They propose a metric that they call eff@k which is the equivalent for pass@k but adapted to the problem of evaluating the performance of code. They then evaluate 30 LLMs (closed and open-source LLMs) on their benchmark using the eff@k metric. They show that state-of-the-art LLMs achieve an eff@1 score of 0.47 and an eff@100 score of 0.575. They also propose a hand-optimized version of each of the 142 problems in their benchmark to set a new standard for LLMs.

### Strengths
-	Evaluating whether LLMs can generate efficient code is an important problem, especially with the increasing amount of research on the topic of code synthesis using LLMs and the wide use of LLMs for coding.
-	The authors provide a comprehensive evaluation of 30 LLMs using the proposed benchmark and more importantly, provide a hand-optimized version of each one of the codes in their benchmark which opens the door for more research on the topic.

### Weaknesses
While the proposed work is important, and while the results are interesting, I don’t believe the contribution and novelty of the work are strong enough. There is clearly a degree of novelty in this paper though, and the proposed benchmark is very valuable from a practical point of view.

The problem of measuring the performance of code is well-studied in the compiler community. There are decades of work on the development of methods for automatic code optimization in compilers and methods to measure the success of such methods. Any paper about automatic code optimization. Here is one example of such work:

       “Towards a Statistical Methodology to Evaluate Program Speedups and their Optimisation Techniques”, Sid Touati.

It would be interesting to include examples of such work in the related work section and also include a detailed discussion in the paper about why a simple metric such as “the speedup” (ratio between the execution time of the reference code over the execution time of the synthesized code) is not enough for this problem and a new metric needs to be proposed.

### Questions
-	Can you please include a detailed discussion of why the the speedup metric classically used by the compiler community when evaluating automatic code optimization methods is not enough for your task?
-	For more completeness, can you also include a discussion of such work in the related work section? A starting point would be:  “Towards a Statistical Methodology to Evaluate Program Speedups and their Optimisation Techniques”, Sid Touati.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents ENAMEL, a benchmark for evaluating the efficiency of LLM-generated code, a quality largely overlooked in current assessments. ENAMEL introduces a new efficiency metric, eff@k, and includes expert-designed reference solutions and rigorous test cases to set high standards. Evaluating 30 popular LLMs, the authors find that while many models generate correct code, they fall short in efficiency, particularly with advanced algorithms and optimizations, underscoring the need for further improvements in LLM code synthesis.

### Strengths
1. Clear and fluent presentation. The metric is carefully designed.
2. The evaluation is convincing and indicative.

### Weaknesses
1. The method is very manual. It is hard to scale.
2. The dataset is small. Humaneval was a good metric several years ago at the early stage of code generation. But now, serious evaluation needs a larger scale dataset.

Despite the above, the dataset is still reasonably valuable due to its high quality.

### Questions
1. Why didn't you consider problems from online judges like codeforces? There are plenty of problems with expert-level efficient solutions as a competition-oriented platform.
2. Did you consider a more automatic way of measuring the complexity? It might not be hard to find out that multiple layers of input scale, simply considering log scales, polynomial scales, and exponential scales.

### Soundness
3

### Presentation
4

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
This paper proposes a benchmark suite, named `ENAMEL`, to evaluate the efficiency of code generated by LLMs. The authors propose a novel metric eff@k that measures the efficiency of the generated code accounting for different input sizes. A human expert provides the reference implementation for each task in the benchmark suite. The evaluation with regard to the eff@k metric demonstrates the large gap between the LLM-generated code and the reference implementation.

### Strengths
1. Human expert-provided reference implementations for the benchmark are of high quality.
2. Evaluation provides insights into the efficiency of LLM-generated code.
3. Clear presentation that is easy to follow.

### Weaknesses
1. The novelty of the proposed eff@k metric is not convincing.

The authors mention the insufficiencies of existing efficiency benchmarks in C1 and C2.

a) For C1, the authors mention that if the code execution exceeds the time limit, the actual efficiency is unknown. However, the authors do not demonstrate how frequently this happens in practice. If this is a rare case, then existing benchmarks are still useful. The authors should provide experimental evidence to demonstrate that existing works do give wrong efficiency measurements due to the presence of such cases.

b) For C2, the authors argue that existing works fail to capture the relationship between code efficiency and the sample size k. By looking at Eq. (5), the proposed solution of ENAMEL is to take the maximum of the efficiency value, while the existing works take the average. The authors do not justify why taking the maximum is a better choice than taking the average. Such a difference in the metric definition seems to be a minor difference.

2. Lack of evaluation on different test case generation strategies.

The code efficiency can be affected by the testing inputs. Ideally, the efficiency should be measured against the worst-case inputs, which can be hard to define in practice. A practical approximation is to take the maximum execution time over a set of testing inputs. As such, the testing input generation is crucial for the efficiency evaluation. It is not clear how strong the test case generation strategy adopted in this paper is. The authors should evaluate the robustness of the proposed eff@k metric against different test case generation strategies.

3. Lack of guidance on setting the hyperparameters for the eff@k metric.

The eff@k metric has a set of hyperparameters, such as $\alpha$ and $h$. The value of these hyperparameters directly affects the efficiency measurement. Without guidance on how to set these hyperparameters, the practical usage of the eff@k metric is limited. It would be better if automatic hyperparameter selection methods were provided; or at least, empirical studies on how the eff@k metric is affected by different hyperparameters.

4. The benchmark suite is limited only to the HumanEval dataset.

This concerns about the generalizability of ENAMEL. The HumanEval dataset contains many simple tasks that require $\mathcal{O}(1)$ time complexity. A potential concern is that the dataset after filtering out those simple tasks may not be large enough to provide a comprehensive evaluation of the efficiency of LLM-generated code.

a) The authors should provide the size and proportion of the remaining tasks after filtering out the simple tasks.

b) The authors can consider extending the benchmark suite to more competitive datasets, such as the CodeContests dataset.

### Questions
1. Why is the maximum efficiency value chosen in the eff@k metric, rather than the average efficiency value?
2. Do the eff@k metric and the existing efficiency metrics give different efficiency rankings for the same LLM-generated code?
3. How sensitive is the eff@k metric to the hyperparameters?
4. What is the size of the ENAMEL benchmark suite?
5. How does the ENAMEL benchmark perform on more competitive datasets, such as the CodeContests dataset?
6. How does the eff@k metric perform on different test case generation strategies?

### Soundness
2

### Presentation
3

### Contribution
3
