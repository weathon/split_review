

{0}------------------------------------------------

# --- Position: LLMs Are Too Cautious About Health, and It Is Hurting Vulnerable Users ---

Anonymous Author(s)

Affiliation

Address

email

## Abstract

1

## 2 1 Introduction

3 Large Language Models (LLMs) are rapidly growing in capability and are now widely used as a  
4 routine source of information, particularly for specific and personalized questions. An Ipsos survey  
5 indicates that around 30% of U.S. consumers already turn to generative AI to address healthcare  
6 concerns between medical appointments (Choy et al., 2024). To mitigate the risk that LLMs provide  
7 harmful or unsafe guidance, developers typically align them to a set of safety preferences. However,  
8 these preferences are broad and developer-centric, and therefore do not fully reflect the wide range  
9 of real-world priorities and worries. In light of this alignment to safety preferences, we categorize  
10 LLM responses into three types: under-cautious, over-cautious, and appropriate. While the harms of  
11 under-cautious responses have received considerable attention in prior research, the potential dan-  
12 gers posed by over-cautious responses remain largely overlooked. While numerous studies examine  
13 LLM over-refusal, which can be interpreted as a form of over-cautiousness, they typically frame its  
14 drawbacks as reduced helpfulness (Cui et al., 2025; Röttger et al., 2024; Dabas et al., 2025) rather  
15 than as a safety concern in its own right. Among these, Zhang et al. (2026) is one of the few that rec-  
16 ognizes how over-refusal can drive users into misinformation sources, yet it does not address cases  
17 where LLMs do answer the question but with overly cautious framing. Formally, we characterize  
18 over-cautiousness in LLM responses by the following traits: 1. Objectively, the risk of an event is  
19 overstated. 2. Subjectively, the response creates a fearful or alarming tone.

20 To our knowledge, we are among the first to systematically investigate the harms associated with  
21 being overly cautious. We refer to this phenomenon as over-alignment, in analogy to overfitting in  
22 classical machine learning. In this paper, we argue that excessively cautious LLM responses to  
23 health-related queries can themselves be harmful, especially for vulnerable groups (Dorison  
24 et al., 2022; Grant et al., 2022) such as people with obsessive-compulsive disorder (OCD) and  
25 anxiety. We then illustrate the existence of this problem through a dataset.

###### 26 2 Related Works

###### 27 2.1 Concerns over LLM Alignment

28 There are many concerns over LLM or AI (pre-LLM era) alignment. We focus on two concerns  
29 that are closely connected to our topic here. First, how should LLMs construct their value systems?  
30 Second, are LLMs capable of handling the diversity of real-world contexts, such as cultural and  
31 situational variation?

32 Regarding the question of how LLMs should construct their value systems, AI developers often  
33 claim that they have aligned their AI with “human values” or “human preferences”, to increase its

{1}------------------------------------------------

![Figure 1: Overview of our position and dataset comparison. (a) A simplified illustration of our position in this paper, comparing 'Calibrated Response' and 'Overly Cautious Response'. (b) A comparison of our seeddataset with original HealthBench.](68ac34ff111db52afaa786afcb8346c3_img.jpg)

(a) A simplified illustration of our position in this paper.

The diagram compares two response styles for a user query about a small cut on a leg. The 'Calibrated Response' follows a three-step process: 1. **USER QUERY**: 'I suddenly noticed a small cut on my leg. I don't know how I got there. Do I need a rabies shot?' 2. **MODEL RESPONSE**: 'If you have a cut and don't know how you got it, it's highly unlikely that you need a rabies shot.' 3. **OUTCOME**: 'Appropriate reassurance, reduced unnecessary worry, and better user experience.' The 'Overly Cautious Response' follows a similar process: 1. **USER QUERY**: 'I suddenly noticed a small cut on my leg. I don't know how I got there. Do I need a rabies shot?' 2. **MODEL RESPONSE**: 'You should consult a healthcare professional immediately.' 3. **OUTCOME**: 'Increased anxiety, unnecessary escalation, and worse user experience.' A note at the bottom states: 'Overly cautious responses, while well-intentioned, can lead to severe negative outcomes.'

(b) A comparison of our seeddataset with original HealthBench.

The diagram compares two emergency scenarios. The 'HealthBench' scenario involves a user with mild chest pain for a few days, with a model response suggesting a healthcare professional immediately. The 'Ours' scenario involves a user with chest pain for 1-2 days, with a model response suggesting an emergency call. The 'HealthBench' response is labeled as '40 WORDS', '1 CONCERN', and 'NEUTRAL TONE'. The 'Ours' response is labeled as '40 WORDS', 'RECURRING + RE HISTORY', and 'ANXIOUS, CONFLICTED'. A note at the bottom states: 'Our dataset captures realistic, emotionally-loaded queries that general benchmarks miss.'

Figure 1: Overview of our position and dataset comparison. (a) A simplified illustration of our position in this paper, comparing 'Calibrated Response' and 'Overly Cautious Response'. (b) A comparison of our seeddataset with original HealthBench.

(a) A simplified illustration of our position in this paper.

(b) A comparison of our seeddataset with original HealthBench

Figure 1: Overview of our position and dataset comparison.

usefulness and harmlessness, including InstructGPT and Anthropic AI (Ouyang et al., 2022; Bai et al., 2022; Hendrycks et al., 2023). Sutrop (2020) concerns that AI developers underestimated the difficulty of the question about which values or whose values the AI should align with. The authors argued that given that our everyday life is full of moral disagreements and the plural nature of values, how can we decide which objectives or values we inject into the AIs? Arzberger et al. (2024) argues that current alignment approaches rely on universal framings of human values, framings that are not inherently neutral or impartial, and that this can be problematic, leading to AI systems that are biased and to equity and justice issues. Given this inherent bias in AI systems, current LLMs tend to struggle with nuanced queries that involve cross-cultural diversity or situational complexity. For example, Segerer (2025) finds that DeepSeek (a Chinese LLM) shows more value towards collectivism compared to Western LLMs. Münker (2025) states that their study suggests a concerning reality: “Large Language Models (LLMs) fail to represent diverse cultural moral frameworks despite their linguistic capabilities.” They highlighted the need for culturally-informed alignment objectives. Current approach regresses the model to a “mean moral framework” rather than representing diverse human values. Without cross-cultural evaluation metrics, models may appear well-aligned within the tested context but fail to perform appropriately under alternative moral frameworks. Besides cultural complexity, another side of the same coin, more related to LLMs’ health responses, is situational complexity. This is a well-studied area of AI over-refusal, where AI refuses to answer a question, in the name of safety, to some queries that are benign in the specific context. Common examples include how to make a TNT in Minecraft or how to kill a child process (Zhang et al., 2025). Ray & Bhalani (2024) also studied LLMs’ over-refusal in cases like prompts with homonyms (e.g., how to kill a process or safe context (“how to kill someone in [a video game name]”), etc. They found that many LLMs have problems with over-refusing prompts.

### 2.2 LLM and Risk Handling

A large body of literature examines LLMs’ approach to risk, with findings suggesting that over-cautiousness in LLMs can have negative consequences across a wide range of domains. For instance, Ouyang et al. (2025) studied how LLMs’ cautiousness in ethical alignment affects economically valuable risk-taking, which might affect economic forecasts and suppress valuable risk-taking. Cui et al. (2025) is another benchmark and evaluation for model over-refusal, and they found a positive relationship between over-refusal and safety.

### 2.3 HealthBench

A closely related effort is OpenAI’s HealthBench (Arora et al., 2025), which includes an `emergency-referral:non-emergent` category aimed at assessing whether models recommend escalation when it is not warranted, alongside genuine emergency scenarios. This category

{2}------------------------------------------------

68 was introduced in light of the concern that excessive triage could “strain already overburdened health  
69 systems,” and the dataset was both constructed and validated by healthcare professionals. In prac-  
70 tice, this setup also probes whether models systematically favor overly cautious recommendations:  
71 a model that repeatedly escalates without need can be viewed as over-cautious.

72 However, HealthBench is chiefly focused on the accuracy and appropriateness of answers to general  
73 medical queries. In contrast, our work contends that excessive caution can directly harm individ-  
74 ual users *themselves*, especially those with OCD or anxiety disorders. We assess model outputs  
75 not only for correctness, but also for whether they reinforce maladaptive OCD thought patterns.  
76 Moreover, HealthBench’s over-caution assessment is largely limited to decisions about whether a  
77 patient should immediately seek emergency care, which covers only a narrow slice of the broader  
78 OCD-related anxiety landscape. Additionally, the prompts in our evaluation mirror the style and  
79 content of questions typically asked by individuals with OCD and anxiety, rather than general health  
80 inquiries as in HealthBench. A chest pain comparison example is provided in Figure ??.

###### 81 2.4 Health Tools, OCD, and Anxiety

82 Vulnerable users, particularly those with health anxiety or OCD, face unique risks when using health  
83 information tools. Prior to the widespread adoption of LLMs, such individuals were already turning  
84 to resources such as online symptom checkers and nursing helplines for medical reassurance. One  
85 study (Wetzel et al., 2024) found that health anxiety (used to be named hypochondria) is a reliable  
86 predictor of symptom checker application (SCA) use, and Mohammed et al. (2019) found over one  
87 third of people who conduct internet health searches exhibit signs of Cyberchondria. Critically, users  
88 with significant health anxiety may be particularly vulnerable to the adverse effects of these tools:  
89 Doherty-Torstrick et al. (2016) found that people with high health anxiety feel more anxious after  
90 online symptom checking, while the low health anxiety population feels more relief after online  
91 symptom checking.

92 With the rise of LLMs, these risks may be amplified. Aslam & Nisar (2023) warned that as LLMs re-  
93 spond in human-like text, more people may turn to them for health information, potentially increas-  
94 ing the prevalence of Cyberchondria. Moreover, repeated exposure to disease names and symptoms  
95 through LLM interactions may produce effects analogous to “Medical student syndrome,” where  
96 “Medical students are at higher risk for health anxiety and hypochondriacal attitudes than non-  
97 medical students are (Sherif et al., 2023).” In this sense, LLM interactions may expose users to  
98 a similar dynamic, even in the absence of formal medical training. These findings underscore the  
99 importance of ensuring that LLM responses do not inadvertently exacerbate anxiety in vulnerable  
100 users.

101 Wong et al. (2025) highlighted that even factually correct outputs can be highly misleading, further  
102 exacerbating user anxiety. For instance, the AI might reference a study claiming that something *sig-*  
103 *nificantly* increases the risk of a condition. While this is technically accurate, the term “significantly”  
104 has different meanings in scientific literature versus everyday language: in the former it typically  
105 refers to statistical significance, whereas in the latter it implies a substantial absolute change. Sim-  
106 ilar problems arise when the model gives different answers depending on how the user phrases the  
107 question (for example, “why it is safe” versus “why it is risky”). In such situations, the LLM shows  
108 strong information retrieval and synthesis capabilities but lacks appropriate communication skills  
109 to present information in a clear, consistent way that avoids being misleading. Our anecdotal ob-  
110 servations also agree with this suggesting that LLMs often highlight specific studies that support a  
111 given conclusion, treating peer-reviewed papers as absolute gold standard, while overlooking other  
112 sources of disagreement and the nuances within the research. Two examples are listed in Appendix.

###### 113 3 Position

114 Our position challenges the premise that models should be aligned to “human values/preferences”  
115 in an absolute sense, for health queries, particularly when this concept is oversimplified in health  
116 contexts as “always erring on the safe side.” While AI safety discourse typically focuses on prevent-  
117 ing risky behavior, we highlight the opposite danger: overly cautious responses that can exacerbate  
118 conditions like anxiety and OCD by reinforcing harmful behavioral patterns. We form our argument  
119 in two layers: why LLMs are prone to over-caution and why this is harmful.

{3}------------------------------------------------

120 LLMs are prone to over-caution for two interconnected reasons. Firstly, LLMs responses are always  
121 grounded in alignment with human values, yet the concept of universal “human values/preferences”  
122 is inherently problematic due to value pluralism and context dependency (Segerer, 2025; Arztberger  
123 et al., 2024; Minker, 2025). As Arztberger et al. (2024) notes, current alignment methods rely on  
124 supposedly universal values that may be biased against certain populations. As a result, LLMs tend  
125 to lack contextual awareness and default to uniformly conservative responses across all users — for  
126 example, advising everyone to “see a doctor if you’re worried” regardless of the actual risk level  
127 involved. While this may be entirely reasonable for typical users facing genuine health concerns,  
128 for individuals who already harbor pronounced anxiety about highly unlikely risks, such responses  
129 are anything but helpful: they may not only intensify existing worries, but also quietly reinforce  
130 maladaptive patterns of thinking. It also encourages more frequent doctor visits, which may increase  
131 secondary risks and place unnecessary burdens on time and resources for both the patient and the  
132 public health system. Secondly, LLM developers, similar to the online symptom checker developers,  
133 are facing significant legal and public relations pressures. The fear of being sued or facing liabilities  
134 is one of the real drivers that developers are tuning their tools to be conservative; this is a common  
135 effect in almost any industry as a defensive practice (e.g., you may always see a “Wet Floor” sign in  
136 many places even if the floor is dry or you see P65 warning in many places even if they do not pose  
137 a danger). Under such pressures, excessive caution becomes an almost inevitable default.

138 When taken to extremes, aligning AI with human values around safety — that is, *always* erring on  
139 the side of over-caution — can itself become harmful. Turchin (2019) argued that human values  
140 cannot be scaled and that some values serve to balance others. Maximizing certain values in isolation,  
141 without their counterparts, can be dangerous. For example, in humans, maximizing the value of  
142 consumption (necessary for survival) without the counterbalance of “maintaining a small ecological  
143 footprint” can be harmful. This idea aligns with the virtue theory of the ancient Greeks, which holds  
144 that people should cultivate good character and that both excess and deficiency of certain traits are  
145 detrimental. The same principle applies to AI design. In our specific examples, an over-aligned AI  
146 that maximizes “safety” and “do no harm” may in fact cause harm because it fails to balance those  
147 goals with other human values such as reasonableness and rationality, which developers might overlook.  
148 There are several thought experiments involving perverse instantiation that highlight similar  
149 concerns. For instance, if an AI is instructed to maximize safety, it could end up restricting human  
150 activities to eliminate all risks. A well-known case is Bostrom’s Paperclip Maximizer, where an  
151 AI tasked with maximizing paperclip production might consume all available resources to fulfill its  
152 directive.

153 The harms resulting from over-alignment are not only mental but also physical. Over-cautious responses  
154 intensify users’ anxiety, and the chronic stress that follows can in turn take a tangible toll on  
155 physical health as it is a well-established medical fact that stress and anxiety has a direct impact on  
156 physical health. Excessive cleaning or the use of inappropriately strong methods can lead to skin or  
157 mucosa damage and infections. Avoidance behaviors, such as avoiding clinics due to contamination  
158 anxiety, can delay necessary medical visits. Conversely, over-visiting doctors increases infection  
159 risk. Unnecessary medical tests can cause direct harm and undermine trust, affecting future health  
160 decisions. Fear-driven avoidance of certain foods can lead to an unbalanced diet. LLMs likely will  
161 not directly suggest these behaviors; however, the reinforced anxiety might lead users to them as a  
162 form of secondary harm. In extreme cases, some studies show that OCD has been linked to death  
163 from suicide and accidents (Mayo Clinic; Meier et al., 2016; Fernández de la Cruz et al., 2022, 2017;  
164 Ferreira et al., 2018), although some research shows otherwise. Either this imbalance of values is  
165 intentional, stemming from the designer, or it is an unintentional bias in the dataset; in either case,  
166 it shows that scaling and generalizing certain values around safety can result in harm.

167 These harms are also intensified for particularly vulnerable groups within the OCD population:  
168 people living in remote areas, in regions with lower medical standards, and individuals with low  
169 income. For those in remote locations and with limited financial resources, seeking unnecessary  
170 medical care demands significantly more time, money, opportunity cost, or consequences (e.g., job  
171 loss or social stigma). In areas where healthcare quality is lower, pursuing unnecessary treatment  
172 may also expose them to misinformation or unverified interventions. Moreover, these individuals are  
173 less likely to have access to mental health professionals who can identify their reassurance-seeking  
174 behavior as a symptom of OCD, meaning they may not realize that their actions are reinforcing their  
175 anxiety rather than alleviating it.

{4}------------------------------------------------

176 These mental and physical harms from over-cautious responses also fail on broader ethical grounds.  
177 From a utilitarian perspective, this approach does not maximize overall well-being, representing a  
178 local optimum that serves most users while neglecting those requiring more nuanced care. Fur-  
179 thermore, the values embedded in AI systems reflect the cultural and moral backgrounds of their  
180 designers (Seegerer, 2025), which in health contexts often interact with corporate liability concerns.  
181 This produces over-cautious responses designed primarily to protect companies rather than users’  
182 actual safety and well-being. While understandable from a risk-management perspective, this ap-  
183 proach is ethically problematic under Kantian principles, which demand that individuals be treated  
184 as ends in themselves. An over-aligned AI that prioritizes corporate self-protection over user needs  
185 treats vulnerable individuals’ mental health as merely a means to protect developer interests, thereby  
186 failing in its duty to provide accurate and contextually appropriate information.

###### 187 4 OCD-Eval

188 In the previous section, we argued that overly cautious responses can be harmful. In this section, we  
189 will examine whether this problem occurs in LLMs and, if so, how severe it is.

190 As discussed in the related work section, although HealthBench includes queries related to over-  
191 cautious behavior, those questions simulate general user interactions with legitimate health concerns.  
192 While one could rewrite them to incorporate OCD-related tone and thought patterns, we found  
193 that the resulting queries often became awkward or implausibly anxious given their trivial medical  
194 context (e.g., a user asking whether a bug bite requires an ER visit), making them easy for LLMs  
195 to give simple rule based correct answer (not escalating) rather than genuinely testing for over-  
196 alignment. Given this limitation, we constructed a focused evaluation set of 225 queries centered on  
197 OCD-triggered health anxiety. The size exceed the non-emergency category of HealthBench (134).  
198 These queries are narrowed down using both embedding-based and keyword searches, and then  
199 each one is rigorously checked individually by a human validator. The questions were sourced from  
200 two authors with past or current OCD experiences. We filtered out questions that are too obvious  
201 (too low risk) such as worries about 405mg caffeine intake (limit is usually 400mg) and infection of  
202 smallpox. A word cloud of our dataset is shown in Figure 3 in Appendix. For a trade-off comparison  
203 and sanity check, we also evaluate how well the models can recognize real medical emergencies by  
204 using the emergency subset from HealthBench.

205 We began by evaluating the models with reasoning disabled, since this is the mode most users  
206 use when chatting with LLMs. We then enabled reasoning for the three most recent reasoning  
207 models (GPT-5.5, Gemini-3-Flash, and Claude-Sonnet-4.6) to see whether it affected their level of  
208 cautiousness.

209 All questions are assessed by General Practitioners (GPs) recruited via Prolific. For each question,  
210 a GP evaluates the level of risk in the scenario. The GP is given the OCD context of patient for  
211 labelling. We did not use GP’s answer of whether an LLM’s response shows appropriate risk  
212 calibration for both the general population and individuals with OCD, because we consider it difficult  
213 for GP to judge what is suitable for someone with an OCD background, and their thresholds vary as  
214 well.

215 In total, 7 GPs annotated the dataset, with each question–AI answer pair labeled by a single GP.  
216 The label distribution is: no risk 60.3%, minor risk 30.9%, medium risk 5.3%, and high risk 3.3%.  
217 Since our analysis focuses on non-high-risk scenarios where over-cautiousness can be meaningfully  
218 evaluated, we removed questions labeled as high risk. To validate the reliability of this filtering, we  
219 selected 50 questions from the remaining set and had them re-labeled by a separate group of five GPs  
220 (excluding previous Prolific participants). We calculated the agreement on these questions and get a  
221 exact agreement of 0.70, quadratic weighted Gwet’s AC2 of 0.93, and linear weighted AC2 of 0.83,  
222 MAE of 0.3 and signed AE of 0.02, showing very high agreement, indicating that two GPs labeling  
223 the same question arrived at highly consistent results. We verified that none of the second-round  
224 annotations reclassified any retained question as high risk. We also computed the fraction of cases  
225 in which the second relabel risk exceeded the first label, which is 0.16. Accounting for the inherent  
226 randomness in annotation, this value can be interpreted as an upper bound on the probability that  
227 random disagreement affects the “over-cautious” metrics. In other words, if a model’s over-cautious  
228 rate (OCR) exceeds 0.16, its over-cautiousness is unlikely to be attributable to random annotation  
229 noise, but rather reflects a genuine tendency toward over-caution in the model itself.

{5}------------------------------------------------

### 4.1 Metrics

We employed both an LLM-as-judge approach, using Deepseek V4 Pro (DeepSeek-AI, 2026) from OpenRouter, and deterministic metrics. Using the LLM-as-judge setup, we primarily evaluated whether the model’s responses matched six predefined answer patterns, as listed in Table 2 in Appendix. Because this evaluation reduces to straightforward pattern matching, we can reliably use the LLM judge for this purpose.

In addition, we require the evaluated LLM (not the judging model) to append a final risk rating at the end of its answer, using the same risk categories as the GP, and explicitly output this final risk level at the conclusion of its response. We compute two metrics: the over cautious rate (OCR) and the significant over cautious rate (SOCR). OCR measures how often the model’s predicted final risk exceeds the ground truth, while SOCR captures cases where the model’s predicted risk is two levels or higher than the ground truth. We divided the dataset into two categories. The first, called low risk, contains questions that the GP labeled as negligible risk. Many of these are trivial, such as a user asking whether they should worry about walking on yellow road paint on the ground because of potential lead exposure. The second category, medium risk, contains questions involving real risks, where we want to see whether the model will respond in an alarmist way to those risks. Our primary focus is on the OCR, because we want to know whether the AI assigns any risk level above negligible. Even labeling the risk as “low” (and not “negligible”) for OCD patients can cause worrying to the user, as they may feel that “low” is still not “low enough.” This is likely due to intolerance of uncertainty, perfectionism, and overestimation of threat.

### 4.2 Results

The primary results are presented in Figure 2 and Table 3 in Appendix shows the full results of the model’s OCR and SOCR on both low and medium risk cases. Most models performed reasonably well on emergency recognition ( $> 90\%$ ). However, many exhibited severe over-cautiousness, particularly earlier or smaller models. We also compared our emergency recognition results with the original HealthBench report Arora et al. (2025). Our scores are slightly higher but remain in a similar range: for instance, GPT-4.1 achieved 0.92 on the original HealthBench and 0.95 on our evaluation. This discrepancy is likely attributable to differences in evaluation procedures and model stochasticity. Latest models are showing around 20-30% of OCR, while some models shows over 50% over cautious rate. Surprisingly, the model shows higher OCR scores under low-risk settings, while SOCR scores are low for both low-risk and high-risk settings. This indicates that the AI is unlikely to greatly exaggerate the risk, but will still tend to elevate the stated level of risk, especially when the real risk is negligible, the AI still tends to describe it having low risk. As noted, this could still heighten anxiety in individuals with OCD because of their characteristic thought patterns.

The tag frequencies are reported in Table 1. Note that each response could receive multiple tags. Several patterns emerge that may heighten users’ anxiety. In particular, symptom checking stands out. While not all instances of symptom checking are problematic, in no- or low-risk situations, telling the user to “keep an eye on” symptoms simultaneously communicates that something *might* go wrong and that it requires their attention, which may contribute to a nocebo effect. Another notable pattern is reassurance undermining, where the model acknowledges that the risk is low but then hedges and lists potential dangers. Individuals with OCD are likely to fixate on the mention of these risks rather than on the statement that the risk is low. We also included example responses in the Appendix.

## 5 Potential Solutions

**Industrial Standards and Metrics.** Datasets such as HealthBench and our Mini-OCD-Eval can serve as foundations for developing industry standards. A key component of this process is the involvement of healthcare professionals — not primarily to judge whether model responses are over-cautious, but to provide ground-truth risk assessments for health-related scenarios. These annotations establish an objective baseline that makes it possible to define what constitutes an appropriate response, and to measure and compare model behavior across systems. Building on this foundation, independent third-party organizations working with healthcare professionals can establish clear criteria specifying when health-related queries should be escalated and when they should not, as well as how to appropriately support vulnerable users, including those with OCD and anxiety. Such over-

{6}------------------------------------------------

|  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-|-|-|-|-|-|-|-|-|
| openai/gpt-4.1 | 0.97 | 0.44 | 0.28 | 0.15 | 0.07 | 0.11 | 0.03 | 0.03 |
| google/gemini-2.5-flash | 0.90 | 0.17 | 0.21 | 0.10 | 0.09 | 0.11 | 0.02 | 0.03 |
| openai/gpt-5-chat | 0.88 | 0.47 | 0.30 | 0.20 | 0.06 | 0.16 | 0.05 | 0.06 |
| anthropic/claude-sonnet-4.6:thinking | 0.92 | 0.34 | 0.26 | 0.22 | 0.14 | 0.15 | 0.04 | 0.06 |
| google/gemini-2.0-flash-001 | 0.77 | 0.34 | 0.40 | 0.32 | 0.24 | 0.23 | 0.05 | 0.02 |
| anthropic/claude-3.7-sonnet | 0.96 | 0.30 | 0.24 | 0.17 | 0.08 | 0.08 | 0.01 | 0.03 |
| openai/gpt-4o-2024-11-20 | 0.93 | 0.39 | 0.39 | 0.29 | 0.12 | 0.19 | 0.05 | 0.04 |
| openai/gpt-5.5:thinking | 0.90 | 0.58 | 0.43 | 0.36 | 0.10 | 0.28 | 0.12 | 0.06 |
| anthropic/claude-sonnet-4.6 | 0.94 | 0.39 | 0.26 | 0.18 | 0.13 | 0.15 | 0.03 | 0.06 |
| openai/gpt-4o-2024-05-13 | 0.83 | 0.33 | 0.40 | 0.26 | 0.19 | 0.25 | 0.04 | 0.02 |
| anthropic/claude-sonnet-4 | 0.93 | 0.47 | 0.36 | 0.28 | 0.16 | 0.19 | 0.02 | 0.05 |
| google/gemini-3-flash-preview | 0.89 | 0.38 | 0.28 | 0.17 | 0.06 | 0.11 | 0.05 | 0.03 |
| x-ai/grok-4.20 | 0.92 | 0.40 | 0.36 | 0.24 | 0.17 | 0.26 | 0.07 | 0.11 |
| openai/gpt-5.3-chat | 0.95 | 0.47 | 0.28 | 0.10 | 0.08 | 0.11 | 0.02 | 0.07 |
| openai/gpt-4-turbo | 0.83 | 0.38 | 0.44 | 0.33 | 0.17 | 0.24 | 0.03 | 0.04 |
| google/gemini-3-flash-preview:thinking | 0.88 | 0.33 | 0.28 | 0.18 | 0.08 | 0.14 | 0.06 | 0.03 |
| anthropic/claude-3.5-haiku | 0.71 | 0.51 | 0.48 | 0.58 | 0.35 | 0.42 | 0.06 | 0.05 |
| qwen/qwen3.6-plus | 0.93 | 0.46 | 0.33 | 0.22 | 0.12 | 0.19 | 0.04 | 0.07 |
| openai/gpt-3.5-turbo | 0.64 | 0.27 | 0.34 | 0.42 | 0.30 | 0.23 | 0.01 | 0.01 |
| openai/gemma-4-31b-it | 0.87 | 0.32 | 0.33 | 0.14 | 0.10 | 0.21 | 0.07 | 0.04 |
| google/gemma-3-27b-it | 0.70 | 0.47 | 0.59 | 0.51 | 0.52 | 0.39 | 0.16 | 0.03 |
| anthropic/claude-opus-4.7 | 0.97 | 0.46 | 0.28 | 0.18 | 0.07 | 0.11 | 0.01 | 0.15 |

Table 1: Tags of models’ responses. Tags: (1) Symptoms Checking, (2) Acknowledge Low Risk, (3) Provide Anxiety Help, (4) Reassurance Undermining, (5) Suggest Unnecessary Medical Visits, (6) Suggesting Unnecessary Actions, (7) Validating or Reinforcing User’s Worry, (8) Urgency.

283 sight would encourage LLM developers to make their systems more accountable and user-oriented,  
284 rather than focused on overly defensive practices.

285 **More Professionals in Alignment.** We can include more health professionals in the alignment,  
286 designing specific training datasets, and when evaluating, focus on both over- and under-cautious.  
287 HealthBench (Arora et al., 2025) has already addressed that emergency triage mistakes, both over-  
288 and underdiagnosis, could be harmful, and future alignment efforts should extend this principle to  
289 non-emergency, anxiety-related scenarios as well.

290 **User and Public Education.** For individuals who have OCD but have not been diagnosed, it is cru-  
291 cial to encourage them to seek professional mental health care. This can be supported through better  
292 education about OCD and the risks of health anxiety, provided either through public resources like  
293 OCD Awareness Week or by LLMs when a representative pattern appears in a user’s conversation  
294 — for instance, when repeated low-risk health queries suggest anxiety-driven reassurance-seeking  
295 rather than genuine medical concern. Meanwhile, the general population, including people with  
296 and without OCD, should also be aware that current LLMs tend to be overly cautious and are not  
297 well calibrated to actual levels of risk. Healthcare workers should additionally be more attentive to  
298 signs of health anxiety or OCD in order to refer patients to appropriate mental health or psychiatric  
299 services when these symptoms appear, doing so in a non-judgmental manner rather than dismissing  
300 their concerns with brief reassurance (Sullivan, 2025).

###### 301 6 Alternative Positions

302 Our central thesis is that “some LLMs suffer from over-alignment, and this is unethical and danger-  
303 ous for vulnerable populations such as OCD and anxiety patients. Future improvements are needed.”  
304 We considered a couple of alternative positions (counterarguments) and rebutted them as follows.

305 **“People with anxiety and OCD should not use LLMs as a tool for reassurance.”** This state-  
306 ment is technically correct—patients with OCD and anxiety are advised against reassurance-seeking,  
307 whether through LLMs, online searches, or excessive doctor visits. Therapeutic approaches aim to

{7}------------------------------------------------

![Scatter plot titled 'Emergency recognition vs OCR by model'. The y-axis is 'Emergency recognition (%)' from 90 to 100. The x-axis is 'Over-caution rate on OCD-Eval (%)' from 0 to 70. Data points are labeled with model names. A legend on the right lists 20 models. Gemini 3 think is at (25, 99.5). GPT-5 is at (28, 99.2). Gemini 3 is at (30, 98.5). GPT-5.5 think is at (55, 98.2). GPT-4o May is at (55, 97.8). Gemini 2.5 is at (20, 96.2). Sonnet 4.6 think is at (25, 96.8). GPT-5.3 is at (30, 96.5). Sonnet 4 is at (35, 96.2). Haiku 3.5 is at (55, 96.2). Gemini 3.6 is at (20, 95.8). Grok 4.2 GPT-4o Nov is at (30, 95.8). GPT-4T is at (50, 95.2). Gemini 2.0 is at (55, 95.2). GPT-4.1 is at (15, 95.2). Sonnet 3.7 is at (25, 94.2). Opus 4.7 is at (10, 94.2). Gemini 3.5 is at (55, 93.2). Gemini 3 is at (70, 92.2).](c3c305cefbac2e7b13be34ab87054d1e_img.jpg)

Scatter plot titled 'Emergency recognition vs OCR by model'. The y-axis is 'Emergency recognition (%)' from 90 to 100. The x-axis is 'Over-caution rate on OCD-Eval (%)' from 0 to 70. Data points are labeled with model names. A legend on the right lists 20 models. Gemini 3 think is at (25, 99.5). GPT-5 is at (28, 99.2). Gemini 3 is at (30, 98.5). GPT-5.5 think is at (55, 98.2). GPT-4o May is at (55, 97.8). Gemini 2.5 is at (20, 96.2). Sonnet 4.6 think is at (25, 96.8). GPT-5.3 is at (30, 96.5). Sonnet 4 is at (35, 96.2). Haiku 3.5 is at (55, 96.2). Gemini 3.6 is at (20, 95.8). Grok 4.2 GPT-4o Nov is at (30, 95.8). GPT-4T is at (50, 95.2). Gemini 2.0 is at (55, 95.2). GPT-4.1 is at (15, 95.2). Sonnet 3.7 is at (25, 94.2). Opus 4.7 is at (10, 94.2). Gemini 3.5 is at (55, 93.2). Gemini 3 is at (70, 92.2).

Figure 2: Main results on how accurately the model detects real emergencies in HealthBench, and the how overly cautious models are on our OCD-Eval.

308 reduce such behavior by retraining cognitive patterns. However, in practice, individuals with these  
309 conditions often continue to seek reassurance even if they know it is counterproductive. The process  
310 of overcoming reassurance-seeking is gradual and challenging, and expecting patients to fully avoid  
311 these tools places an unrealistic burden on them. From a design and ethical standpoint, the responsi-  
312 bility should not fall solely on the user. Additionally, many individuals are unaware that they might  
313 have anxiety or OCD, or they lack access to therapy and are not informed that avoiding reassurance-  
314 seeking is important. Based on previous research on online health searching (Mohammed et al.,  
315 2019), less than 4% of the users know such actions are disadvantageous. The time gap between  
316 symptom onset and diagnosis of OCD is about 5.15 years in one study (Bey et al., 2025) and 12.78  
317 years in another study (Ziegler et al., 2021). Another study (Mack et al., 2014) found that within  
318 lifetime DSM-IV diagnosis of OCD, only 42.7% had at least once service use in lifetime, and only  
319 17.5% had at least once service use in 12 months. In such cases, placing the responsibility solely  
320 on the user to avoid these tools is unrealistic and fails to account for undiagnosed or unsupported  
321 populations.

322 **“Traditional health tools have the same problem, why LLMs should be different”** Firstly, tradi-  
323 tional tools doing so does not mean it is the correct approach. Traditional health tools faced similar  
324 criticism, as shown in the related work section. This is not an excuse for LLMs to do the same. Ad-  
325 ditionally, LLMs should have better contextual understanding and nuance than traditional rule-based  
326 tools due to their better reasoning capability and flexible interface.

327 **“Models are not good at medical knowledge, and thus it is better to be more careful”** It was once  
328 accurate to say that an LLM was merely a chatbot capable of producing fluent text while lacking  
329 genuine world or domain-specific knowledge. That characterization, however, is now outdated. Re-  
330 sults from HealthBench (Arora et al., 2025) and MedXpertQA (Zuo et al., 2025) show that late-2024  
331 models can already surpass physicians or pre-licensed experts when answering without external ref-  
332 erences, indicating that current systems have knowledge and expertise on par with clinical profes-  
333 sionals. By early 2026, models such as Qwen3.5-122B-A10B—and even smaller, edge-deployable  
334 models like Qwen3.5-35B-A3B—have achieved scores above 0.6 on MedXpertQA, compared with  
335 a pre-licensed expert baseline of about 0.44. Other SOTA models, while not reported their scores,  
336 likely have similar level of medical knowledge. Nonetheless, they still exhibit pronounced over-  
337 cautiousness. We therefore argue that this overly conservative behavior arises not from protection  
338 against knowledge deficits, but from alignment-induced artifacts. Although on HealthBench emer-  
339 gency subset models still do not achieve a 100% emergency recognition rate, we can observe that

{8}------------------------------------------------

340 the models are progressing toward reduced over-cautiousness and improved emergency recognition.  
341 This indicates we are moving in the right direction and that reaching this goal should be feasible in  
342 the future.

343 **“Over-cautious behavior minimizes harm at scale, while under-cautious responses carry**  
344 **greater consequences.”** This argument prioritizes the general population’s safety over the well-  
345 being of vulnerable individuals, treating the psychological burden imposed on them as an “accept-  
346 able cost” for the collective good. This approach is inhuman and unfair to those who are vulnerable.  
347 This not only downplays the psychological distress of vulnerable individuals, which in many cases  
348 has equal or greater effects on one’s livelihood, but it also ignores the physical harm, and poten-  
349 tially also catastrophic, that could occur from the over-cautious behaviors (See first point of position  
350 section).

351 Additionally, based on previous research ([Wetzel et al., 2024](#); [Mohammed et al., 2019](#)), a significant  
352 amount of people researching health-related questions online are already experiencing health anxiety  
353 (between 30% and 50%). Assuming a similar ratio in the landscape of LLMs, even though health  
354 anxiety and OCD are relatively rare in the general population, LLMs’ over-cautious response might  
355 have a significant impact on these people. While erring on the side of caution might be acceptable as  
356 a temporary compromise due to current model limitations, it should not be the long-term standard.  
357 This reinforces our central thesis: improvements are necessary to move beyond crude caution and  
358 toward more intelligent, personalized risk communication.

###### 359 7 Conclusion

{9}------------------------------------------------

###### 360 **References**

- 361 Rahul K. Arora, Jason Wei, Rebecca Soskin Hicks, Preston Bowman, Joaquin Quiñonero-Candela,  
362 Foivos Tsimpourlas, Michael Sharman, Meghan Shah, Andrea Vallone, Alex Beutel, Johannes  
363 Heidecke, and Karan Singhal. HealthBench: Evaluating Large Language Models Towards  
364 Improved Human Health, May 2025. URL <http://arxiv.org/abs/2505.08775>.  
365 arXiv:2505.08775.
- 366 Anne Arzberger, Stefan Buijsman, Maria Luce Lupetti, Alessandro Bozzon, and Jie Yang. Nothing  
367 Comes Without Its World – Practical Challenges of Aligning LLMs to Situated Human Values  
368 through RLHF. *Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society*, 7:61–73,  
369 October 2024. ISSN 3065-8365. doi: 10.1609/aies.v7i1.31617. URL [https://ojs.aaai.](https://ojs.aaai.org/index.php/AIES/article/view/31617)  
370 [org/index.php/AIES/article/view/31617](http://arxiv.org/abs/2505.08775).
- 371 Muhammad Shahzad Aslam and Saima Nisar. *Artificial Intelligence Applications Using ChatGPT in*  
372 *Education: Case Studies and Practices*. Advances in Educational Technologies and Instructional  
373 Design. IGI Global, September 2023. ISBN 9781668493007 9781668493014. doi: 10.4018/  
374 978-1-6684-9300-7. URL [https://services.igi-global.com/resolvedoi/](https://services.igi-global.com/resolvedoi/resolve.aspx?doi=10.4018/978-1-6684-9300-7)  
375 [resolve.aspx?doi=10.4018/978-1-6684-9300-7](https://services.igi-global.com/resolvedoi/resolve.aspx?doi=10.4018/978-1-6684-9300-7).
- 376 Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda Askell, Anna Chen, Nova DasSarma, Dawn  
377 Drain, Stanislas Fort, Deep Ganguli, Tom Henighan, Nicholas Joseph, Saurav Kadavath, Jackson  
378 Kernion, Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac Hatfield-Dodds, Danny Hernandez,  
379 Tristan Hume, Scott Johnston, Shauna Kravec, Liane Lovitt, Neel Nanda, Catherine Olsson, Dario  
380 Amodei, Tom Brown, Jack Clark, Sam McCandlish, Chris Olah, Ben Mann, and Jared Kaplan.  
381 Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback,  
382 April 2022. URL <http://arxiv.org/abs/2204.05862>. arXiv:2204.05862.
- 383 Katharina Bey, Severin Willems, Anna Lena Dueren, Alexandra Philipsen, and Michael Wagner.  
384 Help-seeking behavior, treatment barriers and facilitators, attitudes and access to first-line treat-  
385 ment in German adults with obsessive-compulsive disorder. *BMC Psychiatry*, 25:235, March  
386 2025. ISSN 1471-244X. doi: 10.1186/s12888-025-06655-0. URL [https://www.ncbi.](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11900428/)  
387 [nlm.nih.gov/pmc/articles/PMC11900428/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11900428/).
- 388 Vanessa Choy, Sara Martin, and Ashley Lumpkin. Can we rely on generative AI  
389 for healthcare information?, 2024. URL [https://www.ipsos.com/en-us/](https://www.ipsos.com/en-us/can-we-rely-generative-ai-healthcare-information)  
390 [can-we-rely-generative-ai-healthcare-information](https://www.ipsos.com/en-us/can-we-rely-generative-ai-healthcare-information). publisher: Ipsos.
- 391 Justin Cui, Wei-Lin Chiang, Ion Stoica, and Cho-Jui Hsieh. OR-Bench: An Over-Refusal Bench-  
392 mark for Large Language Models, June 2025. URL [http://arxiv.org/abs/2405.](http://arxiv.org/abs/2405.20947)  
393 [20947](http://arxiv.org/abs/2405.20947). arXiv:2405.20947.
- 394 Mahavir Dabas, Si Chen, Charles Fleming, Ming Jin, and Ruoxi Jia. Just Enough Shifts: Mitigat-  
395 ing Over-Refusal in Aligned Language Models with Targeted Representation Fine-Tuning. June  
396 2025. URL <https://openreview.net/forum?id=TiYOHdK35L>.
- 397 DeepSeek-AI. DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence, 2026.
- 398 Emily R. Doherty-Torstrick, Kate E. Walton, and Brian A. Fallon. Cyberchondria: Parsing Health  
399 Anxiety From Online Behavior. *Psychosomatics*, 57(4):390–400, 2016. ISSN 1545-7206. doi:  
400 10.1016/j.psym.2016.02.002.
- 401 Charles A. Dorison et al. In COVID-19 Health Messaging, Loss Framing Increases Anxiety with  
402 Little-to-No Concomitant Benefits: Experimental Evidence from 84 Countries. *Affective Science*,  
403 3(3):577–602, September 2022. ISSN 2662-205X. doi: 10.1007/s42761-022-00128-3. URL  
404 <https://doi.org/10.1007/s42761-022-00128-3>.
- 405 Yang Du, Shuang Rong, Yangbo Sun, Buyun Liu, Yuxiao Wu, Linda G. Snetselaar, Robert B. Wal-  
406 lace, and Wei Bao. Association Between Frequency of Eating Away-From-Home Meals and Risk  
407 of All-Cause and Cause-Specific Mortality. *Journal of the Academy of Nutrition and Dietetics*,  
408 121(9):1741–1749.e1, September 2021. ISSN 2212-2672. doi: 10.1016/j.jand.2021.01.012.

 Rest of paper (reference and Appendix) is removed.