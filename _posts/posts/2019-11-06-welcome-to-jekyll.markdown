---
layout: post
title:  "Welcome to Jekyll!"
date:   2019-11-06 16:50:35 -0600
categories: jekyll update
---
## General Notes

This page is just a page for me to keep little things to reference. It will not be applicable to anyone esle, it's just a convience page for me :)

# MATLAB Connectivity Matrices

The data going into the command `cifti_write_from_template` should be [379,k] where `k` is the number of maps (379 is the number of parcels). Further, given a connectivity matrix that is [379,379], the proper way to reduce this is by

```matlab
nData = [sum(hyper_mask,1); sum(hypo_mask,1)]';
cifti_write_from_template(g,nData,'connMask2.pscalar.nii');
```

# Launch novnc

```bash
sudo novnc --listen 1234 --vnc localhost:5901
```

# Note
I'm just keeping the default page made by jekyll for convience

You’ll find this post in your `_posts` directory. Go ahead and edit it and re-build the site to see your changes. You can rebuild the site in many different ways, but the most common way is to run `jekyll serve`, which launches a web server and auto-regenerates your site when a file is updated.

Jekyll requires blog post files to be named according to the following format:

`YEAR-MONTH-DAY-title.MARKUP`

Where `YEAR` is a four-digit number, `MONTH` and `DAY` are both two-digit numbers, and `MARKUP` is the file extension representing the format used in the file. After that, include the necessary front matter. Take a look at the source for this post to get an idea about how it works.

Jekyll also offers powerful support for code snippets:

{% highlight ruby %}
def print_hi(name)
  puts "Hi, #{name}"
end
print_hi('Tom')
#=> prints 'Hi, Tom' to STDOUT.
{% endhighlight %}

Check out the [Jekyll docs][jekyll-docs] for more info on how to get the most out of Jekyll. File all bugs/feature requests at [Jekyll’s GitHub repo][jekyll-gh]. If you have questions, you can ask them on [Jekyll Talk][jekyll-talk].

[jekyll-docs]: https://jekyllrb.com/docs/home
[jekyll-gh]:   https://github.com/jekyll/jekyll
[jekyll-talk]: https://talk.jekyllrb.com/
