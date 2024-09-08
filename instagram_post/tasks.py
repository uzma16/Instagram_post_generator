from crewai import Task
from textwrap import dedent

class MarketingAnalysisTasks:
	def product_analysis(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			Analyze the given product website: {product_website}.
			Extra details provided by the customer: {product_details}.

			Focus on identifying unique features, benefits,
			and the overall narrative presented.

			Your final report should clearly articulate the
			product's key selling points, its market appeal,
			and suggestions for enhancement or positioning.
			Emphasize the aspects that make the product stand out.

			Keep in mind, attention to detail is crucial for
			a comprehensive analysis. It's currently 2024.
			"""),
			agent=agent,
			expected_output='A detailed report outlining the product’s unique features, benefits, and market appeal, along with suggestions for enhancement or positioning. The report should be comprehensive and highlight what makes the product distinctive.'
		)


	def competitor_analysis(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			Explore competitors of: {product_website}.
			Extra details provided by the customer: {product_details}.

			Identify the top 3 competitors and analyze their
			strategies, market positioning, and customer perception.

			Your final report MUST include BOTH all context about {product_website}
			and a detailed comparison to whatever competitors they have.
			"""),
			agent=agent,
			expected_output='A comprehensive report detailing the strategies, market positioning, and customer perception of the top 3 competitors, including a side-by-side comparison with {product_website}. The report should highlight key differences and potential areas for competitive advantage.'
		)


	def campaign_development(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			You're creating a targeted marketing campaign for: {product_website}.
			Extra details provided by the customer: {product_details}.

			To start this campaign, we will need a strategy and creative content ideas.
			It should be meticulously designed to captivate and engage
			the product's target audience.

			Based on your ideas, your co-workers will create the content for the campaign.

			Your final answer MUST include ideas that will resonate with the audience and
			also include ALL context you have about the product and the customer.
			"""),
			agent=agent,
			expected_output='A detailed marketing strategy and a set of creative content ideas that align with the product’s brand identity and appeal to the target audience. The output should include actionable steps and conceptual outlines for the campaign, ensuring all ideas are primed for content creation and resonate with the market.'
		)


	def instagram_ad_copy(self, agent):
		return Task(description=dedent("""\
			Craft an engaging Instagram post copy.
			The copy should be punchy, captivating, concise,
			and aligned with the product marketing strategy.

			Focus on creating a message that resonates with
			the target audience and highlights the product's
			unique selling points.

			Your ad copy must be attention-grabbing and should
			encourage viewers to take action, whether it's
			visiting the website, making a purchase, or learning
			more about the product.

			Your final answer MUST be 3 options for an ad copy for Instagram that
			not only informs but also excites and persuades the audience.
			"""),
			agent=agent,
			expected_output='Three distinct Instagram ad copies, each designed to be engaging, concise, and action-oriented. Each copy should effectively communicate the product’s value and compel the audience to take specific actions such as visiting the website or making a purchase. The copies should vary in style or approach to cater to different audience preferences.'
		)


	def take_photograph_task(self, agent, copy, product_website, product_details):
		return Task(description=dedent(f"""\
			You are working on a new campaign for a super important customer,
			and you MUST take the most amazing photo ever for an Instagram post
			regarding the product, you have the following copy:
			{copy}

			This is the product you are working with: {product_website}.
			Extra details provided by the customer: {product_details}.

			Imagine what the photo you want to take describes it in a paragraph.
			Here are some examples for you to follow:
			- high-tech airplane in a beautiful blue sky at sunset, super crisp, beautiful 4k, professional wide shot
			- the Last Supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- a bearded old man in the snow, wearing very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Think creatively and focus on how the image can capture the audience's
			attention. Don't show the actual product in the photo.

			Your final answer must be 3 options of photographs, each with 1 paragraph
			describing the photograph exactly like the examples provided above.
			"""),
			agent=agent,
			expected_output='Three detailed and imaginative descriptions of potential photographs for the Instagram campaign. Each description should vividly paint the scene, specifying visual details such as composition, lighting, and resolution, similar to the provided examples. The descriptions should not include the product but should align with the campaign’s theme to engage the target audience effectively.'
		)


	def review_photo(self, agent, product_website, product_details):
		return Task(description=dedent(f"""\
			Review the photos you got from the senior photographer.
			Make sure it's the best possible and aligned with the product's goals,
			review, approve, ask clarifying questions or delegate follow-up work if
			necessary to make decisions. When delegating work, send the full draft
			as part of the information.

			This is the product you are working with: {product_website}.
			Extra details provided by the customer: {product_details}.

			Here are some examples of how the final photographs should look like:
			- high-tech airplane in a beautiful blue sky at sunset, super crisp, beautiful 4k, professional wide shot
			- the Last Supper, with Jesus and his disciples, breaking bread, close shot, soft lighting, 4k, crisp
			- a bearded old man in the snow, wearing very warm clothing, with mountains full of snow behind him, soft lighting, 4k, crisp, close up to the camera

			Your final answer must be 3 reviewed options of photographs,
			each with 1 paragraph description following the examples provided above.
			"""),
			agent=agent,
			expected_output='Three critically reviewed descriptions of photographs, with each description refining and potentially improving upon the initial submissions. The output should clearly state whether each photo is approved, needs modifications, or requires further clarification to meet the product’s marketing goals. Each description should be detailed, addressing composition, alignment with marketing strategy, and overall impact.'
		)
