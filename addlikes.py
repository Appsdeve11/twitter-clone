from flask import jsonify

@app.route('/post/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get_or_404(post_id)

    if current_user in post.likes:
        post.likes.remove(current_user)
        liked = False
    else:
        post.likes.append(current_user)
        liked = True

    db.session.commit()
    return jsonify({'liked': liked, 'like_count': len(post.likes)})