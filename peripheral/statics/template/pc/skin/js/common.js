(function($) {

    $.goup = function(user_params) {

        /* Default Params */
        var params = $.extend({
            location: 'right',
            locationOffset: 20,
            bottomOffset: 10,
            containerRadius: 10,
            containerClass: 'goup-container',
            arrowClass: 'goup-arrow',
            alwaysVisible: false,
            trigger: 500,
            entryAnimation: 'fade',
            goupSpeed: 'slow',
            hideUnderWidth: 500,
            containerColor: '#000',
            arrowColor: '#fff',
            title: '',
            titleAsText: false,
            titleAsTextClass: 'goup-text'
        }, user_params);
        /* */


        $('body').append('<div style="display:none" class="' + params.containerClass + '"></div>');
        var container = $('.' + params.containerClass);
        $(container).html('<div class="' + params.arrowClass + '"></div>');
        var arrow = $('.' + params.arrowClass);

        /* Parameters check */
        var location = params.location;
        if (location != 'right' && location != 'left') {
            location = 'right';
        }

        var locationOffset = params.locationOffset;
        if (locationOffset < 0) {
            locationOffset = 0;
        }

        var bottomOffset = params.bottomOffset;
        if (bottomOffset < 0) {
            bottomOffset = 0;
        }

        var containerRadius = params.containerRadius
        if (containerRadius < 0) {
            containerRadius = 0;
        }

        var trigger = params.trigger;
        if (trigger < 0) {
            trigger = 0;
        }

        var hideUnderWidth = params.hideUnderWidth;
        if (hideUnderWidth < 0) {
            hideUnderWidth = 0;
        }

        var checkColor = /(^#[0-9A-F]{6}$)|(^#[0-9A-F]{3}$)/i;
        if (checkColor.test(params.containerColor)) {
            var containerColor = params.containerColor;
        } else {
            var containerColor = '#000';
        }
        if (checkColor.test(params.arrowColor)) {
            var arrowColor = params.arrowColor;
        } else {
            var arrowColor = '#fff';
        }

        if (params.title === '') {
            params.titleAsText = false;
        }
        /* */

        /* Container Style */
        var containerStyle = {};
        containerStyle = {
            position: 'fixed',
            width: 40,
            height: 40,
            background: containerColor,
            cursor: 'pointer'
        };
        containerStyle['bottom'] = bottomOffset;
        containerStyle[location] = locationOffset;
        containerStyle['border-radius'] = containerRadius;

        $(container).css(containerStyle);
        if (!params.titleAsText) {
            $(container).attr('title', params.title);
        } else {
            $('body').append('<div class="' + params.titleAsTextClass + '">' + params.title + '</div>');
            var textContainer = $('.' + params.titleAsTextClass);
            $(textContainer).attr('style', $(container).attr('style'));
            $(textContainer).css('background', 'transparent')
                .css('width', 80)
                .css('height', 'auto')
                .css('text-align', 'center')
                .css(location, locationOffset - 20);
            var containerNewBottom = $(textContainer).height() + 10;
            $(container).css('bottom', '+=' + containerNewBottom + 'px');
        }


        /* Arrow Style */
        var arrowStyle = {};
        arrowStyle = {
            width: 0,
            height: 0,
            margin: '0 auto',
            'padding-top': 13,
            'border-style': 'solid',
            'border-width': '0 10px 10px 10px',
            'border-color': 'transparent transparent ' + arrowColor + ' transparent'
        };
        $(arrow).css(arrowStyle);
        /* */



        /* Trigger Hide under a certain width */
        var isHidden = false;
        $(window).resize(function() {
            if ($(window).outerWidth() <= hideUnderWidth) {
                isHidden = true;
                do_animation($(container), 'hide', params.entryAnimation);
                if (textContainer)
                    do_animation($(textContainer), 'hide', params.entryAnimation);
            } else {
                isHidden = false;
                $(window).trigger('scroll');
            }
        });
        /* If i load the page under a certain width, i don't have the event 'resize' */
        if ($(window).outerWidth() <= hideUnderWidth) {
            isHidden = true;
            $(container).hide();
            if (textContainer)
                $(textContainer).hide();
        }


        /* Trigger show event */
        if (!params.alwaysVisible) {
            $(window).scroll(function() {
                if ($(window).scrollTop() >= trigger && !isHidden) {
                    do_animation($(container), 'show', params.entryAnimation);
                    if (textContainer)
                        do_animation($(textContainer), 'show', params.entryAnimation);
                }

                if ($(window).scrollTop() < trigger && !isHidden) {
                    do_animation($(container), 'hide', params.entryAnimation);
                    if (textContainer)
                        do_animation($(textContainer), 'hide', params.entryAnimation);
                }
            });
        } else {
            do_animation($(container), 'show', params.entryAnimation);
            if (textContainer)
                do_animation($(textContainer), 'show', params.entryAnimation);
        }
        /* If i load the page and the scroll is over the trigger, i don't have immediately the event 'scroll' */
        if ($(window).scrollTop() >= trigger && !isHidden) {
            do_animation($(container), 'show', params.entryAnimation);
            if (textContainer)
                do_animation($(textContainer), 'show', params.entryAnimation);
        }

        /* Click event */
        $(container).on('click', function() {
            $('html,body').animate({
                scrollTop: 0
            }, params.goupSpeed);
            return false;
        });

        $(textContainer).on('click', function() {
            $('html,body').animate({
                scrollTop: 0
            }, params.goupSpeed);
            return false;
        });
    };


    /* Private function for the animation */
    function do_animation(obj, type, animation) {
        if (type == 'show') {
            switch (animation) {
                case 'fade':
                    obj.fadeIn();
                    break;

                case 'slide':
                    obj.slideDown();
                    break;

                default:
                    obj.fadeIn();
            }
        } else {
            switch (animation) {
                case 'fade':
                    obj.fadeOut();
                    break;

                case 'slide':
                    obj.slideUp();
                    break;

                default:
                    obj.fadeOut();
            }
        }
    }

}(jQuery));

$(document).ready(function() {
    // 弹窗搜索--------------------------;
    $('#search').click(function() {
        $('.search').toggle(400);
        $('.header-m2').toggle(100);
    });

    $('.header-m2').on('click', function(event) {
        $('.search').hide(400);
        $('.tantel').hide(400);
        $(this).hide(100);

    });
    var h = $(".index-lanmu-main img").height();
    $(".arrow").height(h);
    $(window).resize(function() {
        var h = $(".index-lanmu-main img").height();
        $(".arrow").height(h);
    });

    var w = $(window).width();
    $('.index-lanmu-main').width(w - 120);
    $(window).resize(function() {
        var w = $(window).width();
        $('.index-lanmu-main').width(w - 120);
    });

    var m = 0;
    var lr = 0;

    $('.left-arrow').click(function() {
        var jlr = $('#lanm-ul').offset().left;
        if (jlr < 15) {
            lr = jlr + $("#lanm-ul li").width();
            if (jlr > -$("#lanm-ul li").width()) {
                $("#lanm-ul").animate({
                    marginLeft: "0px"
                }, 500);
            } else {
                $("#lanm-ul").animate({
                    marginLeft: lr + "px"
                }, 500);
            }

            lr = lr - $("#lanm-ul li").width();
            m = 0;
        }
        if (jlr > 15) {
            $("#lanm-ul").animate({
                marginLeft: "0px"
            }, 500);
            layer.msg('没有了！', {
                icon: 5
            });
            lr = 0;
        }

    });
    $('.right-arrow').click(function() {
        var jl = $('#lanm-ul>li:last').offset().left + $("#lanm-ul li").width() + 60;
        if (jl > $(window).width()) {
            m = m - $("#lanm-ul li").width();
            $("#lanm-ul").animate({
                marginLeft: m + "px"
            }, 500);
            lr = 0;
        }
        if (jl < $(window).width() - 60) {
            $('#lanm-ul>li:last').animate({
                marginRight: "0px"
            }, 500);
            layer.msg('没有了！', {
                icon: 5
            });
            m = 0;
        }

    });

    // 去除没有颜色值的选项--------------------------;
    $('.color-v').each(function(index, el) {
        var data_color = $(this).attr('data-color');
        if (data_color == '') {
            $(this).hide();
        }
    });
    // 点击不同颜色点显示不同颜色-----------------------;
    $('.color-v').on('click', function(event) {
        $(this).addClass('icon-duigou').siblings().removeClass('icon-duigou');
        var aid = $(this).attr('data-id');
        var imgurl = $(this).attr('data-color');
        var colorv = $(this).attr('color');
        colorv = parseInt(colorv.split('').reverse().join(''), 16);
        if (colorv > 11645361) {
            $(this).css('color', '#000000');
        }
        $('.pro-' + aid).attr('src', imgurl);
    });
    // 多选筛选条件-----------------------------------;
    $('.nav1 .other').on('click', function() {
        var auth_list = [];
        $(".filtr-item").hide();
        $(this).toggleClass('active1');
        $(".all").removeClass('active1');
        $(".active1").each(function(index, val) {
            auth_list.push($(this).attr('data-multifilter'));
        });
        var new_arr = [];
        for (var i = 0; i < auth_list.length; i++) {　　
            var items = auth_list[i];　　 //判断元素是否存在于new_arr中，如果不存在则插入到new_arr的最后
            　　
            if ($.inArray(items, new_arr) == -1) {　　　　
                new_arr.push(items);　　
            }
        }
        $(".filtr-item").each(function(index, val) {
            var arr = $(this).attr("data-category").split(',');
            if (isContained(arr, new_arr)) {
                $(this).show();
            };
        });
    });
    $(".all").on('click', function() {
        $(this).toggleClass('active1').siblings().removeClass('active1');
        $(".filtr-item").show();
    });

    function isContained(a, b) {
        if (!(a instanceof Array) || !(b instanceof Array)) return false;
        if (a.length < b.length) return false;
        var aStr = a.toString();
        for (var i = 0, len = b.length; i < len; i++) {
            if (aStr.indexOf(b[i]) == -1) return false;
        }
        return true;
    }


    // 头部下拉菜单-----------------------------------;
    var i = 0;
    $('#lanmu').on('click', function(event) {
        $('.down-lanmu').slideToggle(800);
        if (i == 0) {
            $(this).removeClass('icon--lanmuguanli');
            $(this).addClass('icon-cross-fill');
            $('.header-m').show();
            i = 1;
        } else {
            $(this).removeClass('icon-cross-fill');
            $(this).addClass('icon--lanmuguanli');
            $('.header-m').hide();
            i = 0;
        }

    });
    $('.header-m').on('click', function(event) {

        if (i == 0) {
            $('#lanmu').removeClass('icon--lanmuguanli');
            $('#lanmu').addClass('icon-cross-fill');

            $(this).show();
            i = 1;
        } else {
            $('.down-lanmu').hide(800);
            $('#lanmu').removeClass('icon-cross-fill');
            $('#lanmu').addClass('icon--lanmuguanli');
            $(this).hide();
            i = 0;
        }
    });

    $('.canshu-xiala').on('click', function(event) {
        var id = $(this).attr('data-id');
        var classv = $(this).attr('data-class');
        $('#' + id).slideToggle(800);
        if (classv == 'icon-jia') {
            $(this).removeClass('icon-jia');
            $(this).addClass('icon-cha');
            $(this).attr('data-class', 'icon-cha');
        } else {
            $(this).removeClass('icon-cha');
            $(this).addClass('icon-jia');
            $(this).attr('data-class', 'icon-jia');
        }

    });
    $.goup({
        trigger: 100,
        bottomOffset: 100,
        locationOffset: 60,
        title: 'To top',
        titleAsText: true
    });

});