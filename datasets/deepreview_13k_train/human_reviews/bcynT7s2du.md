# Can Generative AI Solve Your In-Context Learning Problem?  A Martingale Perspective

- Decision: Accept
- Scores: 5, 8, 6

## Abstract
This work is about estimating when a conditional generative model (CGM) can solve an in-context learning (ICL) problem.
    An in-context learning (ICL) problem comprises a CGM, a dataset, and a prediction task.
    The CGM could be a multi-modal foundation model; the dataset, a collection of patient histories, test results, and recorded diagnoses; and the prediction task to communicate a diagnosis to a new patient.
    A Bayesian interpretation of ICL assumes that the CGM computes a posterior predictive distribution over an unknown Bayesian model defining a joint distribution over latent explanations and observable data.
    From this perspective, Bayesian model criticism is a reasonable approach to assess the suitability of a given CGM for an ICL problem.
    However, such approaches---like posterior predictive checks (PPCs)---often assume that we can sample from the likelihood and posterior defined by the Bayesian model, which are not explicitly given for contemporary CGMs.
    To address this, we show when ancestral sampling from the predictive distribution of a CGM is equivalent to sampling datasets from the posterior predictive of the assumed Bayesian model.
    Then we develop the generative predictive $p$-value, which enables PPCs and their cousins for contemporary CGMs.
    The generative predictive $p$-value can then be used in a statistical decision procedure to determine when the model is appropriate for an ICL problem.
    Our method only requires generating queries and responses from a CGM and evaluating its response log probability.
    We empirically evaluate our method on synthetic tabular, imaging, and natural language ICL tasks using large language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The current paper aims to quantify whether a conditional generative model (e.g., an LLM) can solve an in-context learning problem. To achieve this goal, authors relate the problem to that Bayesian model criticism, i.e., how decent a model are we currently using for solving the task at hand. Since the hypothesis used by, e.g., an LLM to solve an ICL task is bound to be unclear, the paper relies on use of the posterior predictive distribution for achieving its goal. Specifically, the authors use posterior predictive checks to perform model criticism. Results show proposed tests correlate with model abilities to solve an ICL task.

### Strengths
What I enjoyed the most about this paper is its really nice, pedagogical writing: even though no particularly new concepts were proposed in the technical sections, the slowly developing pace to contextualize ICL within a Bayesian framework made for a really enjoyable read. This did however take away a lot of space, leading to the experimental section becoming rather sparse on discussion.

### Weaknesses
- My main apprehension is that the targeted problem of "what ICL problem can a generative model solve" wasn't sufficiently clarified, leading to confusion in regards to how the results should be interpreted. For example, if the goal is to judge whether my model can solve a task in-context, can I not just evaluate on said task via a benchmark and get a performance estimate (e.g., accuracy)? What else do tests like posterior predictive check offer? In fact, results in the paper (e.g., see Figure 6) show that proposed metrics and accuracy follow an almost one-to-one mapping with respect to each other. Thus, I could have just accuracy as an estimate of how well the model performs the task (if at all). To address this comment, I would request authors to clarify what exactly is a good standard for an answer to the question what ICL problem can a generative model solve. If it's to make a predictive test, i.e., something I can use to preemptively say my model is incapable of performing some task, then I think the currently proposed measures don't fall under that definition.

- At Line 231, authors say when the discrepancy of the data generated under the model is greater than that of the holdout data, then we can be confident that the model explains the holdout data well. This seems unintuitive: if the model generates the data, wouldn't it have a relatively high likelihood it, especially compared to holdout data that it did not generate?

### Questions
See limitations.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors consider the problem of determining whether a CGM can solve an ICL task. Taking a Bayesian view of ICL, the authors use Bayesian model criticism techniques (e.g., PPCs) to tackle this problem. The primary technical challenge is that CGMs don’t expose the posterior and likelihood which are required for certain types of discrepancy functions. The authors then introduce a practical estimator for the posterior predictive p-value that involves repeated ancestral sampling from the predictive distribution of the CGM and show this is equivalent (asymptotically) to posterior predictive p-value. The authors evaluate their method of detecting whether LLMs can solve ICL tasks in synthetic and real-world settings.

### Strengths
I think the framework is interesting. There are lots of papers that view ICL through a Bayesian lens, but this paper is pretty unique in introducing and leveraging this perspective for model criticism. I think the theoretical formulation of this problem through the lens of Bayesian model criticism helped me better understand ICL. 

The theoretical results/perspective motivate a fairly intuitive, practical, and general estimator: drawing samples from the CGM and using those samples to form a null distribution over some discrepancy function and then computing a p-value using that empirical null distribution. It’s nice that this intuitive approach emerges naturally from a Bayesian perspective, although I'm curious if people have introduced a similar method before but motivated in a more ad-hoc way. 

The writing was generally clear, and there was enough background to help me understand the technical details.

### Weaknesses
My biggest concern is: could the authors elaborate more on what they think are compelling, practical use cases? I think right now, the empirical evaluation doesn’t quite do this line of work justice; I’ll elaborate more below, but that being said, I’m open to updating/revising my assessment, given the author’s response. 

The method is presented as a way to estimate when a CGM can solve an ICL task. Can’t you often just directly evaluate this, though? For example, you could sample from a CGM and ask a domain expert or write some program to evaluate the responses. For example, in Experiment 3, you actually have ground truth labels for the queries, right? You already know that Llama-2 7B can’t solve the MQP task, so what additional value does this method provide? 

I think the value of this method would be more apparent in settings (1) where ground truth labels are very hard to source and (2) there’s ambiguity about whether a given ICL task is “in-capability” or “out-of-capability.” Adding some additional evaluation on those sorts of tasks would strengthen the submission.  

Another question I have is: to what extent do we need discrepancy functions that rely on having the model likelihood and model posterior explicitly? If you choose g to be the log marginal model likelihood (as I think you do in some of the experiments), you can estimate the posterior predictive p-value exactly right (I think this is the “Lite” generative prediction p-value algorithm)? I guess it’s not totally clear to me that the NLL method is reliably better. I don't think this significantly diminishes the importance of developing a practical estimator for situations where you need access to the likelihood, and this probably depends on the task, but I would appreciate a more thorough discussion of how to choose a good g(). 

In practice, the martingale p-value incurs estimation error. I would've liked to see some synthetic experiments that analyze this empirically. For example, how large does N need to be for the approximation to be good? I suspect there's a fairly simple experiment here where you consider some model where the likelihood and posterior are available. 

There are a few places where the writing could be improved. For example, when you define the generative process involving f, it might help to give some concrete examples of what that actually means in a practical ICL task. Also, two different discrepancy functions were introduced in Section 5, but you only need the ancestral sampling-based estimator (introduced in Section 5) when you use the second discrepancy function. I think I was a bit confused when I read Section 6 after Section 6.

### Questions
Some minor comments/questions 

I’m not very familiar with the theory underlying PPCs, but I don’t think the posterior predictive p-values always share the theoretical properties of frequentist p-values (e.g., uniformly distributed under the null except maybe when the test statistic is ancillary). Is the same true for martingale p-values and does this have any practical implications? 

The notation |(z_i, y_i)| was a bit confusing to me. I think this refers to the number of tokens comprising the pair of query and response? 

In the abstract, “is equivalent sampling” -> “is equivalent to sampling".

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
2

### Summary
This paper studies how the tools and terminology from Bayesian modelling can be applied to in-context learning with LLMs. 

The paper has ten pages. 

The first six pages introduce a lot of terminology from Bayesian modelling and ask how this is connected with the auto-regressive next token objective from the LLM. The authors make plausible that the terminology from Bayesian modelling offers a useful perspective on LLM in-context learning and derive a Theorem that shows that "the martingale predictive p-value is equal to the posterior predictive p-value."

The last four pages of the paper centre around a simple empirical application. The authors evaluate Llama-2 7B and Gemma 9B on a synthetic regression task, as well as on SST2 and MedicalQP. They find that the small models handle SST2 well but perform no better than random on MedicalQP.

The paper is overall well-written and sound. However, its research contribution is not significant enough for ICLR.

### Strengths
The paper's topic, how tools from Bayesian analysis can be useful to understand in-context learning with LLMs, is interesting.

The paper is well-written in the sense that its language and structure are clear. I also like the expressive section headings. 

I did not check the details of the proofs, but both the theoretical arguments in the paper and the experimental results make sense.

### Weaknesses
While the topic of the paper is interesting and the paper is well-written, neither the theoretical nor empirical results in this paper are strong enough to warrant acceptance at ICLR.

The insight that there are connections between in-context learning and Bayesian methods is not novel (https://arxiv.org/pdf/2111.02080). While the first 6 pages of this paper offer a nice methodological discussion, it remains unclear what the research contribution is (apart from Theorem 2, which seems to be a relatively straightforward result).

The experimental analysis is limited to a synthetic regression task and two real-world datasets. The performance difference between SST2 and MQP for the small models is so striking that I do not believe we would need any of the Bayesian tools offered in this paper to see this.  

Given the motivation in the first paragraph of the paper. I think think the Medprompt paper is a missing reference: https://arxiv.org/abs/2311.16452

### Questions
Why are there no references in the first two paragraphs of the paper? In general, I find many points in this paper where references are required. 

Figure 1: What is the meaning of the different model responses? Did you sample? If yes, at what temperature?

Why did you choose SST-2 and MQP? Why Llama-2 7B model?

Why not consider a bigger model (e.g. Llama-3 405B) and see if it can perform better than random on MQP?

"ancestral sampling": At the end of the day, is this just a fancy term to describe how you are doing standard sampling of the next token from the language model? You are introducing a lot of terminology in this paper, and it is not always clear whether this is required (also: "explanation", "library")

After discussion period:
========================

After the discussion with the authors, I have decided to increase my score to 6.

The generative predictive p-value is an interesting concept. The authors believe that it has the potential to improve upon existing techniques, and I find their arguments broadly plausible. This concept might be of interest to the ICLR community. 

Reason for why not higher score: 

Even though the authors provided additional experiments as part of the rebuttal, this paper's experimental section is still a weak spot. 

Concretely, I don't think that the current version of the experiments makes a sufficiently strong case for the usefulness of the generative predictive p-value, in the way in which the authors claimed that it can be useful during the rebuttal. The reader who is not genuinely interested in the Bayesian motivation and theory behind the generative predictive p-values is not sufficiently convinced by the presented experiments. The particular experiments in this paper are also not connected to the recent literature on in-context learning (at least, I don't see a strong connection). For example, there are, at this point, already several different papers that study in-context learning with LLMs and tabular data, and it is unclear how the experiments in this paper relate to the overall results in the literature. 

It is a minor point, but some aspects of the experimental section are also not particularly well done, such as the descriptions of the figures.

### Soundness
3

### Presentation
3

### Contribution
2
