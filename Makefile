production:
	middleman contentful && middleman build && cp netlify_headers _site/_headers

deploy_preview:
	middleman contentful && middleman build && cp netlify_headers _site/_headers

branch_deploy:
	middleman contentful && middleman build && cp netlify_headers _site/_headers
