/**
 * WebSocket Bus service
 * @function
 * @param {Object} $rootScope
 * @param {Object} logger
 * @param {String} configURL
 * @return {Object} service
 */
function WSBusService($rootScope, logger, configURL) {
    let ws;

    /**
     * Init function
     * @function
     * @param {string} url
     */
    function init(url) {
        ws = new WebSocket(url);
        ws.onopen = function() {};
        ws.onmessage = function(e) {
            let res = JSON.parse(e.data);
            processWSMessage(res);
        };
        ws.onerror = function(e) {
            logger.log('WS error: ', e);
        };
        ws.onclose = function(e) {
            init(url);
        };
        service.ws = ws;
    }

    /**
     * Proces Web socket Message
     * @function
     * @param {Object} msg
     */
    function processWSMessage(msg) {
        $rootScope.$broadcast('ds.wsBus:notify', msg);
    }

    let service = {
        init: init,
        ws: ws,
        url: configURL,
    };

    return service;
}

/**
 * Web Socket Bus Service Provider
 * @class
 */
export class WSBusServiceProvider {
    /**
     * Constructor
     */
    constructor() {
        this.configURL = '';
        this.setUrl = (url) => {
            this.configURL = url;
        };
    }

    /* @ngInject*/
    /**
     * $get
     * @function
     * @param {Object} $rootScope
     * @param {Object}  logger
     * @return {function} WSBusService
     */
    $get($rootScope, logger) {
        return new WSBusService($rootScope, logger, this.configURL);
    }
}
