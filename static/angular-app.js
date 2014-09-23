App = angular.module('App', ['ngResource', 'datePicker']);

App.factory('ArticleServices', ['$resource', function($resource){
  return $resource('article', {}, {
    'query': {method:'GET', isArray: true}
  });
}]);

App.factory('ArticleServices', ['$resource', function($resource){
  return $resource('article/:id', {}, {
    get: {method:'GET', param: {id: '@id'}},
    update: {method:'PUT', param: {id: '@id'}},
    delete: {method:'DELETE', param: {id: '@id'}}
  });
}]);

App.controller('ArticleCtrl', ['$scope', 'ArticleServices', function($scope, Article) {
  $scope.articleList = Article.query();
  $scope.orderProp = 'code';

  $scope.create = function() {
    $scope.article_id = 0;
    $scope.article_code = undefined;
    $scope.article_title = undefined;
    $scope.article_posttime = undefined;
    $scope.article_remark = undefined;
  };

  $scope.edit = function(article) {
    Article.get({id: article.id}, function(article) {
      $scope.article_id = article.id;
      $scope.article_code = article.code;
      $scope.article_title = article.title;
      $scope.article_posttime = article.posttime;
      $scope.article_remark = article.remark;
    });
  };

  $scope.removeAlert = function(article) {
    Article.get({id: article.id}, function(article) {
      $scope.article_id = article.id;
      $scope.article_code = article.code;
      $scope.article_title = article.title;
      $scope.article_posttime = article.posttime;
      $scope.article_remark = article.remark;
    });
  };

  $scope.remove = function() {
    var article_id = $scope.article_id;
    Article.remove({id: article_id}, function(article) {
      $scope.articleList = Article.query();
      $scope.orderProp = 'code';
      $('#deleteModal').modal('hide');
    });
  };

  $scope.submit = function() {
    var posttime = $('#DatePicker').val();
    var article = {
      code: $scope.article_code,
      title: $scope.article_title,
      posttime: posttime,
      remark: $scope.article_remark
    };
    Article.update({id: $scope.article_id}, article, function(item) {
      $scope.articleList = Article.query();
      $scope.orderProp = 'code';
      $('#editModal').modal('hide');
    });
  };

}]);