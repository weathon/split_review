# OSDA Agent: Leveraging Large Language Models for De Novo Design of Organic Structure Directing Agents

- Decision: Accept
- Scores: 8, 8, 8, 6

## Abstract
Zeolites are crystalline porous materials that have been widely utilized in petrochemical industries as well as sustainable chemistry areas. Synthesis of zeolites often requires small molecules termed Organic Structure Directing Agents (OSDAs), which are critical in forming the porous structure. Molecule generation models can aid the design of OSDAs, but they are limited by single functionality and lack of interactivity. Meanwhile, large language models (LLMs) such as GPT-4, as general-purpose artificial intelligence systems, excel in instruction comprehension, logical reasoning, and interactive communication. However, LLMs lack in-depth chemistry knowledge and first-principle computation capabilities, resulting in uncontrollable outcomes even after fine-tuning. In this paper, we propose OSDA Agent, an interactive OSDA design framework that leverages LLMs as the brain, coupled with computational chemistry tools. The OSDA Agent consists of three main components: the Actor, responsible for generating potential OSDA structures; the Evaluator, which assesses and scores the generated OSDAs using computational chemistry tools; and the Self-reflector, which produces reflective summaries based on the Evaluator's feedback to refine the Actor's subsequent outputs. Experiments on representative zeolite frameworks show the generation-evaluation-reflection-refinement workflow can perform de novo design of OSDAs with superior generation quality than the pure LLM model, generating candidates consistent with experimentally validated OSDAs and optimizing known OSDAs. 
The code and model will be publicly available.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces the OSDA Agent, an innovative framework combining Large Language Models (LLMs) with computational chemistry tools for the de novo design of Organic Structure Directing Agents (OSDAs) for zeolites. The framework includes three main components: Actor, Evaluator, and Self-reflector, enhancing the process of generating and optimizing OSDA molecules. Demonstrates significant improvements over existing models in generating OSDAs that are not only theoretically valid but practically feasible. Provides a comprehensive methodological approach and substantial experimental results, setting a new standard in computational chemistry and molecular design.

### Strengths
1. Integrating LLMs with computational chemistry tools to create a feedback-informed molecule generation model is unique. This model addresses the limitations of traditional molecule design models by providing an interactive and iterative design process that includes a novel binding-energy prediction module (Section 4.1). 
2. The experimental design is robust, with clear definitions of metrics and methodological approaches that ensure the reproducibility and validity of results. The use of a layered approach combining different computational tools to assess molecule viability is particularly noteworthy (Sections 5.1 and 5.2). 
3. The paper is well-structured and written, offering detailed explanations of the processes and technologies involved, such as the Actor-Evaluator-Self-reflector framework. Figures and tables effectively illustrate complex processes and results. 
4. This research has a high potential impact, particularly on industries relying on zeolites. Generating and optimizing OSDAs more efficiently could lead to significant advancements in material science and related fields.

### Weaknesses
1. The paper could better address how the proposed model might generalize to other types of molecular design beyond OSDAs for zeolites. It is unclear whether the techniques and improvements reported apply to broader classes of materials or chemical processes. Specifically, the reliance on the specific chemical properties of OSDAs and their interaction with zeolites raises questions about the applicability of the model to molecules with different functional groups or target materials with different binding mechanisms.
2. The reliance on external computational chemistry tools may introduce limitations related to the scalability and speed of the proposed approach. The paper could expand on the implications of these dependencies, particularly in terms of computational cost and accessibility. For instance, the computational cost of the binding energy calculations, which involve molecular docking and energy minimization, is not thoroughly discussed, and it is unclear how this cost scales with the size and complexity of the molecules being evaluated.
3. The models are trained and validated primarily using the Zeolite Organic Structure Directing Agent Database and the Jensen dataset. The diversity and representativeness of these datasets could be questioned, potentially affecting the robustness and applicability of the findings (Section 3.1). The datasets might not fully capture the chemical space of all possible OSDAs, and the model's performance on novel or less represented OSDAs could be limited.

### Questions
1. Can the methodologies and framework presented be adapted to design other types of molecules or materials not discussed in the paper? What changes or adaptations would be necessary? 
2. What are the computational resource requirements for implementing the OSDA Agent framework, significantly when scaling to larger datasets or more complex molecular structures? 
3. How does the framework handle changes or updates in computational chemistry tools or LLMs? Is there a mechanism to easily integrate new tools or updates in knowledge of the field? 
4. Could you elaborate on the choice of evaluation metrics used? How do these metrics align with the practical requirements of OSDA applications in the industry?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces OSDA Agent, a novel framework that combines LLMs (particularly GPT-4) with computational chemistry tools to design Organic Structure Directing Agents (OSDAs) for zeolite synthesis. The framework consists of three key components:

1. An Actor powered by GPT-4 that designs potential OSDAs using few-shot Chain of Thought prompting, In-Context Learning with OSDB database examples, and a memory component for context.

2. An Evaluator that employs computational chemistry tools (RDKit for validity, SCScore for synthesis feasibility) and a novel binding energy model(having an MAE of 0.384 kJ/mol Si) to assess generated structures. 

3. A Self-Reflector using GPT-4o that provides iterative feedback based on evaluations stored in memory to improve chemical validity, synthetic feasibility, and binding energy estimations through a generation-evaluation-reflection-refinement workflow.

The authors validate their framework across multiple zeolite types, demonstrating its ability to generate chemically valid OSDA candidates outperforming the baselines across multiple similatiy metrics. Additionally, the framework successfully optimizes existing OSDA molecules, reducing their synthetic complexity scores from 3.45 to 2.46 while maintaining their functional properties and keeping binding energies within desired ranges (-3.38 to -9.00 kcal/mol). The authors benchmark their experiments against other methods such as MolT5 and BioT5 using diverse metrics including validity, MACCS, and BLEU scores. Subject matter experts have confirmed that the OSDAs designed by the OSDA Agent show the potential to function effectively as structure-directing agents.

### Strengths
- Novel OSDA framework that combines LLMs with chemical validation tools and binding energy models.
- Immense practical significance due to zeolites' widespread industrial applications, making efficient OSDA generation methods valuable.
- Strong experimental results demonstrating OSDA Agent's ability to generate competitive and sometimes superior OSDA designs over baseline methods such as MolT5, BioT5, and pure GPT-4
- Comprehensive evaluation using multiple metrics (validity, similarity, distribution measures) strengthened by validation from domain experts.
- Demonstrated capability to optimize existing OSDA structures by reducing synthetic complexity scores while maintaining functional properties.

### Weaknesses
 - Additional experiments examining the relative importance of different components (e.g., the reflector mechanism) and various tools (RDKit, SCScore, binding energy models), along with analysis of failure patterns (such as consistent failures in chemical validity) would strengthen the paper's findings.
- The paper does not specify the number of iterations used in the design-evaluate-reflect process.  Additional analysis of how metrics change with iterations and when the performance plateaus would be valuable.
- A comparison with domain-specific fine-tuned LLMs or using LLMs other than GPT-4 could strengthen the generalizability of the work.

### Questions
- Could you specify the number of iterations of the OSDA agent (design-evaluate-reflect iterations)? What criteria did you use to determine the optimal number of iterations?

- The paper demonstrates OSDA Agent's success on multiple zeolite types, how does your framework handle increasing zeolite complexity? Are there any known limitations in terms of zeolite structure complexity or OSDA size?

- Could you elaborate on the expert validation process? Specifically, what validation criteria were used, and have any of your generated OSDAs been experimentally synthesized?

- Your framework integrates multiple components (reflection mechanism, multiple aspects in the evaluator such as RDKit, SCScore, and binding energy models). Have you conducted ablation studies to understand their relative importance? For instance, how much does the reflection mechanism contribute to the final performance, and what are the most common types of failures?

- What motivated the choice of using different LLM variants (GPT-4 for the Actor, GPT-4o for the Self-reflector) in your framework? Have you conducted comparative experiments with other LLM combinations, either using the same model for both components or testing with open-source LLMs?

### Soundness
3

### Presentation
3

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
This paper introduces the OSDA Agent, an interactive framework specifically made for designing organic structure directing (OSDA) agents, which is critical for zeolite synthesis. The main goal of the OSDA agent is to generate the de novo design of OSDAs with given zeolites as the target. This framework integrates computational chemistry tools into LLMs to check the quality of generated molecules and includes a reflection mechanism to improve OSDA generation. The OSDA Agent proposed in this work contains three key components: actor, evaluator, and self-reflector. This novel framework design creates a continuous learning environment that would facilitate more efficient and effective zeolite synthesis planning. Experimental results from the paper demonstrate the OSDA Agent yields better quality results compared to existing baseline models.

### Strengths
1. Novel chemistry LLM agent for molecule generation with a reflection mechanism design: the self-reflection modules in the OSDA Agent reuse feedback from previous iterations to optimize future trials, and this enhances the agent's decision-making ability effectively. 
2. Tools to evaluate the quality of generated molecules: this model also includes three chemical tools to check if the generated chemical is valid and feasible, by checking the validity with RDKit, synthetic complexity. To estimate the binding energy, the authors also train their own binding energy estimation model that has lower computational complexity compared to existing computational methods.

### Weaknesses
1. Limited post-generation check: this agent framework includes three chemical property checks, and those would be useful for checking if the generated chemical is valid or reasonable, however, it does not consider other properties such as toxicity and explosiveness, the safety of the chemical in general. 
2. Robustness of the input to the agent model: as there are multiple ways to represent a chemical, does this model support multiple chemical expressions, i.e. chemical formulas like H2O and IUPAC names like oxidane? The 'Evaluator' in the agent model would convert the input target zeolite into a SMILES string, but have you considered changing the chemical expression to see if the 'Evaluator' still works? 
3. Accuracy of binding energy estimation model: this work proposes a new binding energy estimation model to lower the computational complexity of previous computational tools, but how accurate is this estimation model, and is the estimation from this model comparable to traditional atomic simulation methods?  
4. LLM consideration: this work considers OpenAI's GPT models as the base LLM for the agent, and they are not open-source models and would be potentially costly to use, is there any reason that the authors did not also consider open-source models like Llama and Mistral, or would you consider experimenting with those open-source models? 
5. Performances of the baseline models: curious about performance compared to baseline models, specifically for the 'validity' metric the authors proposed, how is this calculated, is it based on results from multiple computational models? This question stems from the result showing that one of the baseline models has a validity score of 0.00 for both datasets whereas the proposed model has a score of 100. 
6. Memory and cost: this agent model includes a reflection mechanism and the paper also shows the number of reflections vs SCScore plot, showing that 4 reflections would reduce the synthesis difficulty, would having more reflections yield even better performances, and what is the cost of reflections? 
7. Safety concerns: do GPT models always fulfill users' requests, and is there any case that the model refuses to fulfill the request or gives out a warning due to safety concerns of the generation process or the chemical itself, or is there any case that the model fails to generate the answer due to its limited knowledge of certain uncommon chemicals?

### Questions
1. Robustness of the input to the agent model: as there are multiple ways to represent a chemical, does this model support multiple chemical expressions, i.e. chemical formulas like H2O and IUPAC names like oxidane? The 'Evaluator' in the agent model would convert the input target zeolite into a SMILES string, but have you considered changing the chemical expression to see if the 'Evaluator' still works? 
2. Accuracy of binding energy estimation model: this work proposes a new binding energy estimation model to lower the computational complexity of previous computational tools, but how accurate is this estimation model, and is the estimation from this model comparable to traditional atomic simulation methods?  
3. LLM consideration: this work considers OpenAI's GPT models as the base LLM for the agent, and they are not open-source models and would be potentially costly to use, is there any reason that the authors did not also consider open-source models like Llama and Mistral, or would you consider experimenting with those open-source models? 
4. Performances of the baseline models: curious about performance compared to baseline models, specifically for the 'validity' metric the authors proposed, how is this calculated, is it based on results from multiple computational models? This question stems from the result showing that one of the baseline models has a validity score of 0.00 for both datasets whereas the proposed model has a score of 100. 
5. Memory and cost: this agent model includes a reflection mechanism and the paper also shows the number of reflections vs SCScore plot, showing that 4 reflections would reduce the synthesis difficulty, would having more reflections yield even better performances, and what is the cost of reflections?
6. Safety concerns: do GPT models always fulfill users' requests, and is there any case that the model refuses to fulfill the request or gives out a warning due to safety concerns of the generation process or the chemical itself, or is there any case that the model fails to generate the answer due to its limited knowledge of certain uncommon chemicals?

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
2

### Summary
The authors introduce OSDA Agent, an interactive framework for designing Organic Structure Directing Agents (OSDAs) used in zeolite synthesis. The framework leverages large language models (LLMs) as the core intelligence, complemented by computational chemistry tools. OSDA Agent consists of three key components: the Actor (generates potential OSDA structures), the Evaluator (assesses generated OSDAs using computational tools), and the Self-reflector (produces reflective summaries to refine subsequent outputs).
The main advantages of OSDA Agent are:

- Improved generation quality compared to pure LLM models, producing candidates consistent with experimentally validated OSDAs.
- Integration of chemical knowledge and tools to ensure generated molecules adhere to chemical rules and are feasible.
- Interactive and iterative design process that leverages feedback and self-reflection

Experiments demonstrate that OSDA Agent outperforms baseline methods, including state-of-the-art text-based de novo molecule generation approaches.

### Strengths
[Algorithm use] The work seems to highlight the successful use of existing LLM pipelines in searching a vast space of objects of scientific discovery. In this case, the objects were chemical agents, OSDAs, but theoretically, these could also be molecules, drugs, equations, etc. It also presents the possibility of connecting LLM pipelines to more traditional algorithms or solutions which allow evaluating the outputs of LLM models and sending feedback to improve future iterations. This is valuable for the community since it shows the viability of prior work.

[Results] Building on the previous strength, the use of the existing methods allowed authors to discover researched OSDAs as well as potentially new ones. This shows the robustness of the framework, possibly opening new avenues to zeolite synthesis. The real consequences of the introduced method are difficult to predict without expert knowledge of the chosen topic.

### Weaknesses
 [Motivation] Being a non-expert in chemistry it is difficult to grasp why OSDAs pose such a challenge to contemporary methods. Linked to that, the description of related work could use some more detail, at least 1 example of an existing method and the way it works with a discussion on how the method presented in this work builds upon its weaknesses. The authors do try to convey that new algorithms for OSDAs are needed but it isn’t clear to me why. Is it only the need to give feedback to the algorithm in order to get better outputs with the next iteration (impossible to achieve with traditional ML methods)? If so, why would it be so crucial for OSDAs? Is it that the current methods are ineffective for some subclass of OSDAs or…?

[Specificity] The work may be certainly worthwhile to OSDA specialists but I have doubts whether it would be of general interest. It shows how to apply an existing framework to a specific task of chemical agent construction. There seems to be limited novelty when it comes to representation learning itself or algorithmics in general. The reflection mechanism that verbalizes errors found by the Evaluator for future learning seems to be taken from a paper by Shin et al. (2024), and adjusted for this particular task, similarly to other used algorithms.

[Clarity] As much as the manuscript is written well and it is possible to understand the syntax and often what is being conveyed, some of the jargon becomes weary and makes details intelligible. This happens in Section 3, where the data is described and seemingly one of the crucial contributions of the work — the binding energy. It is also evident in Section 4.1 —the authors talk about SMILES sequences, In-Context Learning, Chain of Thought, etc. without ever defining, even intuitively, what these acronyms convey. See also RDKit, SCScore, etc. Section 4.1. would benefit from explaining intuition on the framework rather than an overview with specifics defined later.

[Details] There are a lot of moving parts in the whole framework but there is little detail on how they work exactly. Which of the parts are new knowledge? How does the whole framework operate, from start to finish? Each step in the processing could be described in a separate subsection, to streamline presentation.

### Questions
1. Can you provide more context on why OSDAs pose such a challenge to contemporary methods?
2. What specific aspects of OSDA design call for an interactive, feedback-driven approach like the one you've developed? Are there certain subclasses of OSDAs that current methods struggle with?
3. Can you provide an overview of the working of the whole OSDA framework descriptively, without pointing to existing work?
4. How does this work contribute to the broader fields of representation learning or algorithmic design beyond an application of existing methods to OSDA synthesis? Can you elaborate on the novelty of your approach compared to existing frameworks?
5. How does the binding energy estimation model work, and why is it crucial for your approach? Could you explain this concept in more accessible terms?

### Soundness
3

### Presentation
2

### Contribution
2
